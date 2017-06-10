#!/usr/bin/env python2
from __future__ import print_function
import json
import yaml
import sys
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

config = yaml.load(open('./config.yml', 'r'))
program_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
client_id = config["client"]["id"]
client_secret = config["client"]["secret"]
url = "https://api.intra.42.fr"
page_size = 30
campus = 1 # Paris
user_id = "bwaegene"
ft_api = None


def get_acces_token(client_id, client_secret, url):
    client = BackendApplicationClient(client_id=client_id)
    session = OAuth2Session(client=client)
    token = session.fetch_token(token_url=url + "/oauth/token",
                               client_id=client_id,
                               client_secret=client_secret)
    return(session)


def choose_project():
    print()


def print_not_finished_projects():
    '''Print all the projects you didn\'t finished'''
    page = 0
    content = None
    projects = dict()
    print("\033[1mID and name of the projects you didn't finished\033[0m:")
    while page == 0 or len(content) == page_size:
        response = ft_api.get(url + "/v2/users/" + user_id +
                              "/projects_users?page[number]=" + str(page))
        content = json.loads(response.content)
        for project in content:
            if str(project["status"]) != "finished":
                print("%4d: %s" % (project["project"]["id"],
                                   project["project"]["slug"]))
        page = page + 1


def get_project_users(project_id):
    '''Get the list of users which did or are doing a project in your campus'''
    page = 0
    content = None
    users = list()
    while page == 0 or len(content) == page_size:
        response = ft_api.get(url + "/v2/projects/" + str(project_id) +
                              "/projects_users?page[number]=" + str(page) +
                              "&filter[campus]=" + str(campus))
        content = json.loads(response.content)
        for team in content:
            for user in team["teams"][0]["users"]:
                users.append(str(user["login"]))
        page = page + 1
    users = list(set(users))
    users = sorted(users)
    return(users)


def logged_users(users):
    '''Display the users if they are logged in'''
    result = list()
    for user in range(0, len(users)):
        response = ft_api.get(url + "/v2/users/" + users[user])
        content = json.loads(response.content)
        present = content["location"]
        if present != None:
            print(users[user])


def main():
    global ft_api
    ft_api = get_acces_token(client_id, client_secret, url)
    print_not_finished_projects()
    project_id = input("\033[1mEnter the ID of the project you are doing:\033[0m ")
    users = get_project_users(project_id)
    print("\033[1mUsers which did the project and are logged in:\033[0m")
    users = logged_users(users);

if __name__ == "__main__":
    main()
