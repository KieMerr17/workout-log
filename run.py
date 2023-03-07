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


# exercises = SHEET.worksheet('exercises')
# exercise_sheet = exercises.get_all_values()

# results = SHEET.worksheet('results')
# results_sheet = results.get_all_values()

# workouts = SHEET.worksheet('workouts')
# workouts_sheet = workouts.get_all_values()

# Start of Terminal process
print("Welcome to your workout log\n")

users_name = []


def get_users_name():
    user_input = input("Please enter your First and Last name..\n")
    users_name.append(user_input)
    return users_name


def validate_username(user):
    all_names = SHEET.worksheet('names')
    names_list = all_names.get_all_values()
    for name in names_list:
        if name == user:
            print("Located your profile!")
            exit()
    all_names.append_row(user)
    print("*New profile created*")


def main():
    get_users_name()
    validate_username(users_name)


main()
