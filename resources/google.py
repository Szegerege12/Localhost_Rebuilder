from flask import request
from flask_restx import Api, Resource, reqparse
import requests

class Google(Resource):
  def get(self):
    CALENDAR_ID = 'tus8nrv0qvj22iattok736saq4@group.calendar.google.com'
    API_KEY = 'AIzaSyA_f8X_MTGiO4KljzDaddo7wz8lYKeSM4g'

    url = f'https://www.googleapis.com/calendar/v3/calendars/{CALENDAR_ID}/events?key={API_KEY}'

    calendar_events = requests.get(url = url)
    events = calendar_events.json()

    return events, 200


  # ####calendar add events####
  # def post(self):
        
  #   """Returns an authorized API client by discovering the IoT API and creating
  #   a service object using the service account credentials JSON."""
    
  #   api_scopes = SCOPES
  #   api_version = 'v3'
    
  #   audience = 'https://www.googleapis.com/calendar'
  #   service_name = 'calendar'


  #   service_account_info = json.load(open('service_credentials.json'))
  #   credentials = jwt.Credentials.from_service_account_info(service_account_info,
  #     audience=audience)

  #   # with open('service_credentials.json', 'r') as service_account_json:
  #   #   service_account_json = json.load(service_account_json)

  #   #   credentials = service_account.Credentials.from_service_account_info(
  #   #         service_account_json)

  #   #   scoped_credentials = credentials.with_scopes(api_scopes)

  #   # # discovery_url = '{}?version={}'.format(
  #   # #         discovery_api, api_version)

  #   service = build(
  #           service_name,
  #           api_version,
  #           credentials=credentials) 

  #   # AIzaSyBCzwm9eDQ_jP3KyRJNJdpSRBSgzyXpReA
  #   # service = build('calendar', 'v3', credentials=creds)
  #   # service = build('calendar', 'v3', developerKey='AIzaSyCp3ABp9oIBkzz0vWvfMTPWHOdStzvhtUk')

  #   event = {
  #     'summary': 'test argsxxx',
  #     'start': {
  #       'dateTime': '2020-07-04T17:00:00+02:00',
  #       'timeZone': 'Europe/Warsaw',
  #     },
  #     'end': {
  #       'dateTime': '2020-07-04T17:00:00+02:00',
  #       'timeZone': 'Europe/Warsaw',
  #     },
  #     'attendees': [
  #       {'email': 'mrszegerege@gmail.com'},
  #     ],
  #     'reminders': {
  #       'useDefault': False,
  #       'overrides': [
  #         {'method': 'email', 'minutes': 24 * 60},
  #         {'method': 'popup', 'minutes': 10},
  #       ],
  #     },
  #   }
  #   # ee3laqngqhp7m8vqiv5cn5561o@group.calendar.google.com
  #   # tus8nrv0qvj22iattok736saq4@group.calendar.google.com
  #   event = service.events().insert(calendarId='ee3laqngqhp7m8vqiv5cn5561o@group.calendar.google.com', body=event).execute()
  #   data = {
  #     'code':200,
  #     'message':'Pomyślnie utworzono wdarzenie',
  #   }
  #   return data