# Sample code was taken from https://developers.google.com/calendar/quickstart/python

import httplib2
import json

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from pprint import pprint
from dateutil import parser

import datetime


def get_events(service, calendar_id):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=now,
        maxResults=10,
        singleEvents=True,
        orderBy='startTime').execute()
    return events_result.get('items', [])


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    scopes = 'https://www.googleapis.com/auth/calendar.readonly'
    client_secret_file = 'config/client_id.json'
    application_name = 'Nextor'
    credential_file = 'config/google_credentials.json'

    store = Storage(credential_file)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, scopes)
        flow.user_agent = application_name
        credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_file)
    return credentials


def get_weekday(day):
    if day == 0: return "Montag"
    if day == 1: return "Dienstag"
    if day == 2: return "Mittwoch"
    if day == 3: return "Donnerstag"
    if day == 4: return "Freitag"
    if day == 5: return "Samstag"
    if day == 6: return "Sonntag"


def uniform_event(event):
    start = parser.parse(event['start'].get('dateTime', event['start'].get('date')))
    end = parser.parse(event['start'].get('dateTime', event['start'].get('date')))
    # print(dt.weekday())
    date_format = "%d-%m-%Y %H:%M:%S"
    return {
        'summary': event['summary'],
        'start': start.strftime(date_format),
        'end': end.strftime(date_format),
        'weekday': get_weekday(start.weekday())
    }


def calendar(calendar_config):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    full_calender = dict()

    for name, calendar_id in calendar_config.items():
        full_calender[name] = list()
        events = get_events(service, calendar_id)
        for event in events:
            full_calender[name].append(uniform_event(event))
    pprint(full_calender)


if __name__ == '__main__':
    get_credentials()
