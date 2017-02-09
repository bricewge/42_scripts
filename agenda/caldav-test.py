import caldav
import yaml

config = yaml.load(open('./config.yml', 'r'))

URL = config['calendar']['url']
USERNAME = config['calendar']['username']
PASSWORD = config['calendar']['password']

client = caldav.DAVClient(URL, username=USERNAME, password=PASSWORD)
principal = client.principal()
calendars = principal.calendars()
if len(calendars) > 0:
    calendar = calendars[2]
    print ("Using calendar", calendar)
