#!/bin/python2

from __future__ import unicode_literals

from imapclient import IMAPClient

import yaml

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
response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE', 'ENVELOPE'])
for msgid, data in response.iteritems():
    print('   ID %d: %d bytes, flags=%s, subject=%s' % (msgid,
                                                        data[b'RFC822.SIZE'],
                                                        data[b'FLAGS'],
                                                        data['ENVELOPE'].subject))
