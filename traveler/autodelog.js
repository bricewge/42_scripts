const got = require('got');
const yaml = require('js-yaml');
const fs = require('fs');
const FormData = require('form-data');
const os = require("os");

const creds = yaml.safeLoad(fs.readFileSync('../credentials.yml', 'utf8'));
const client_id = creds['client']['id'];
const client_secret = creds['client']['secret'];
const api_url = creds['url'];
var token;

function get_acces_token(client_id, client_secret, api_url)
{

    const form = new FormData();
    form.append('grant_type', 'client_credentials');
    form.append('client_id', client_id);
    form.append('client_secret', client_secret);
    return got.post(api_url + '/oauth/token', { body: form })
        .then(response => { return JSON.parse(response.body)['access_token'];
                          })
        .catch(error => { console.log(error); });
}

function get_user_location()
{
    const user = os.userInfo().username;
    return get_acces_token(client_id, client_secret, api_url)
        .then(token => {
            return got(`${api_url}/v2/users/${user}/locations`,
                { headers: { Authorization: `Bearer ${token}` } })
                .then(response => {
                   return JSON.parse(response.body)[0]['host'];
                })
                .catch(error => { console.log(error); });
        })
        .catch(error => { console.log(error); });
}

function get_current_host()
{
    return os.hostname().split('.')[0];
}

function is_location_saved()
{
    return get_user_location()
        .then(location => {
            process.exit( location === get_current_host() ? 0 : 1);
        });
}

is_location_saved();
