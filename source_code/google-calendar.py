from __future__ import print_function
import datetime
import pickle
import os.path
import pandas as pd
import numpy as np
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']      
      
def convert_datetime_to_duration(start, end):
    
    start = convert_str_to_datetime(start.rstrip('05:30'))
    end = convert_str_to_datetime(end.rstrip('05:30'))
    
    t_delta = end - start
    duration = t_delta.total_seconds()   
    duration = duration / 60
    
    return duration

def convert_str_to_datetime(time_str):
    
    date_format = '%Y-%m-%dT%H:%M:%S+'
    time = datetime.datetime.strptime(time_str, date_format)
    
    return time
    
def parse_datetime(time):
    
    index = time.find('T') + 1
    time = time[index: index + 5]
    
    hour = int(time[0:2])
    minute = int(time[3:5])
    
    if hour < 5:
        hour+=12
    
    return hour, minute
    
    
def create_df_from_events(events, day):
    
    event_dict = {}
    name = []
    duration = []
    start_datetime = []
    color = []
#    end_datetime = []
    
    for event in events:
        start_time = event['start'].get('dateTime')
        name.append(event['summary'])
        duration.append(convert_datetime_to_duration(start_time, event['end'].get('dateTime')))
        start_datetime.append(start_time)
        color.append(event.get('colorId',0))
#        end_datetime.append(event['end'].get('dateTime'))
    
#    event_dict['end_time'] = end_datetime        
    event_dict['start_time'] = start_datetime
    event_dict['event_duration'] = duration
    event_dict['category'] = color
    event_dict['event_name'] = name
    event_dict['day'] = np.ones(len(duration),int) * (day+1)
    
    event_dataframe = pd.DataFrame(event_dict)
    
    return event_dataframe
   
    
def create_dataframe_for_given_dates(service, date, days):
    
    # Convert given date to a datetime object
    date_format = '%b %d, %Y'
    date = datetime.datetime.strptime(date, date_format)
    date = date + datetime.timedelta(hours = 2)
    final_df = pd.DataFrame()
    
    for day in range(days):
        min_time, max_time = calculate_max_min_time(date,day)
#        print('day: {}, min_time: {}, ,max_time: {}'.format(day, min_time, max_time))
        events_result = service.events().list(calendarId='primary', timeMin=min_time,
                                        timeMax=max_time, singleEvents=True,
                                        orderBy='startTime').execute()
        events = events_result.get('items', [])
        final_df = pd.concat([final_df, create_df_from_events(events,day)])

    return final_df


def calculate_max_min_time(date,day):
    
    min_date = date + datetime.timedelta(days = day)
    max_date = min_date + datetime.timedelta(days = 1)
    min_time = min_date.isoformat() + 'Z'
    max_time = max_date.isoformat() + 'Z'
    
    return min_time, max_time


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Enter start date and the number of days that you want data for
    date1 = 'Dec 25, 2019'
    days = 7
    
    df = create_dataframe_for_given_dates(service, date1,days)
    df.to_csv('Last_week_2019.csv', index = False)
    
    print('Data extracted and copied to Last_week_2019.csv')
    
	
if __name__ == '__main__':
    main()