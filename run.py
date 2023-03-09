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


def get_users_name():
    """
    Function gets the First and Last name of the user.
    """
    user_input = input("Please enter your First and Last name..\n")
    return user_input


def get_users_age():
    """
    Function gets the age of the user.
    """
    print("Please enter your age.")
    print("For example '31'")
    user_age = input("")
    return user_age


def validate_username(user):
    """
    Function checks to see if users inputted name is already on 
    the spreadsheet.
    If NOT then it appends the name to the sheet.
    """
    all_names = SHEET.worksheet('profiles')
    names_list = all_names.col_values(1)
    if user in names_list:
        print("Located your profile!")
    else:
        user_age = get_users_age()
        all_names.append_row([user, user_age])

        print("*New profile created*")
    

def main():
    user_name = get_users_name()
    validate_username(user_name)
    

main()
