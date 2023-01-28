from __future__ import print_function
import os

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def insert_row(spreadsheet_id, range_name, value_input_option, 
                  _values):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    if os.path.exists('token.json'):
         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'backend/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    service = build('sheets', 'v4', credentials=creds)
        
    spreadsheet_id = spreadsheet_id
    range_name = range_name
    values = _values
    body = {'range': range_name, 'values': values}

    result = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption='RAW', body=body).execute()
    