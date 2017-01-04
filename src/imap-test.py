#!/bin/python2

from __future__ import unicode_literals

from imapclient import IMAPClient

import yaml
import email

config = yaml.load(open('./config.yml', 'r'))

HOST = config['email']['server']
USERNAME = config['email']['username']
PASSWORD = config['email']['password']
ssl = config['email']['ssl']

server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

select_info = server.select_folder('42')
print('%d messages in 42' % select_info['EXISTS'])

messages = server.search(['NOT', 'DELETED', u'SUBJECT', u'Inscription to'])
print("%d messages that aren't deleted" % len(messages))

print()
print("Messages:")
response = server.fetch([240], ['ENVELOPE', 'RFC822', 'BODY[TEXT]'])
# for msgid, data in response.iteritems():
#     print('subject=%s,\n\n%s' % (
#                                                         data['ENVELOPE'].subject,
#                                                         data['BODY[TEXT]']))
def getEmail():
    print()

def getICSFromMail(mail):
    print(mail)
    for i,part in enumerate(mail.walk(),1):
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get_filename() == 'event.ics':
            print(part.get_payload(decode=True))

getICSFromMail(email.message_from_string(response[240]['RFC822']))
