#!/usr/bin/env python2
from __future__ import print_function
import json
import yaml
import sys
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

program_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
credentials = yaml.load(open('../credentials.yml', 'r'))
client_id = credentials["client"]["id"]
client_secret = credentials["client"]["secret"]
url = credentials["url"]
# Variables to customize
config = yaml.load(open('./config.yml', 'r'))
users = config["users"]


client = BackendApplicationClient(client_id=client_id)
ft_api = OAuth2Session(client=client)
token = ft_api.fetch_token(token_url=url + "/oauth/token",
                           client_id=client_id,
                           client_secret=client_secret)

print(program_name, end=" ")
for i in range(0, len(users)):
    response = ft_api.get(url + "/v2/users/" + users[i])
    result = json.loads(response.content)["location"]
    if result == None:
        result = 0
    else:
        result = 1
    if i < len(users) - 1:
        print(users[i] + "=" + str(result), end=",")
    else:
        print(users[i] + "=" + str(result))
