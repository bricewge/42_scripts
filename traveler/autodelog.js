const got = require('got');
const yaml = require('js-yaml');
const fs = require('fs');
const FormData = require('form-data');


var token;

try {
    const creds = yaml.safeLoad(fs.readFileSync('../credentials.yml', 'utf8'));
    const client_id = creds['client']['id'];
    const client_secret = creds['client']['secret'];
    const api_url = creds['url'];

    const form = new FormData();
    form.append('grant_type', 'client_credentials');
    form.append('client_id', client_id);
    form.append('client_secret', client_secret);
    got.post(api_url + '/oauth/token', { body: form })
        .then(response => { token = JSON.parse(response.body)['access_token'];
                            console.log(token);
                          })
        .catch(error => { console.log(error); });
} catch(e) {
    console.log(e);
}

