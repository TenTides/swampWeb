import sys
import ast 
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

input = ast.literal_eval(sys.argv[1])
for i in input:
    print(i)

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('add_json_file_here.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)