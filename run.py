import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('workout-log')

# Get all sheet information from Google Sheets
names = SHEET.worksheet('names')
name_sheet = names.get_all_values()

exercises = SHEET.worksheet('exercises')
exercise_sheet = exercises.get_all_values()

results = SHEET.worksheet('results')
results_sheet = results.get_all_values()

workouts = SHEET.worksheet('workouts')
workouts_sheet = workouts.get_all_values()

pprint(name_sheet)
pprint(exercise_sheet)
pprint(results_sheet)
pprint(workouts_sheet)