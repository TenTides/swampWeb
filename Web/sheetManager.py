import sys
import ast 
import gspread
import pandas as pd
import json
import ast
from oauth2client.service_account import ServiceAccountCredentials

input = ast.literal_eval(sys.argv[1])
for i in input:
    print(i)

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('add_json_file_here.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

#how to parse a string and return it back to app.js
#input = sys.argv[1]
#output = input
#print(output)
#sys.stdout.flush()

#how to parse an array and return it back to app.js
# data_to_pass_back = "Passed back"
# input = ast.literal_eval(sys.argv[1])
# output = input
# output.append(data_to_pass_back)
# print(json.dumps(output))
# sys.stdout.flush()