"""these are imports duh"""
import os
#import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd

def insert_row(spreadsheet_id, range_name, _values):
    """this is a function to add a row"""          
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'backend/credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w',encoding="utf-8") as token:
            token.write(creds.to_json())
            
    service = build('sheets', 'v4', credentials=creds)
    values = _values
    body = {'range': range_name, 'values': values}
    
    try:
        sheet = service.spreadsheets()# pylint: disable=maybe-no-member
        sheet.values().append(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption='RAW', body=body).execute()
    except HttpError as err:
        print(err)


def sheets_to_df(spreadsheet_id, range_names):
    """this is function to convert a google sheet to a pandas dataframe"""
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'backend/credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w',encoding="utf-8") as token:
            token.write(creds.to_json())
            
    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range_names).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        
        df = pd.DataFrame()
        
        for row in values:
            new_df = pd.DataFrame([row])
            df = pd.concat([df, new_df], axis=0, ignore_index=False)

    except HttpError as err:
        print(err)

    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header 
    
    return df
