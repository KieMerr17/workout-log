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

# Start of Terminal process
print("Welcome to your workout log\n")


def get_users_name():
    """
    Function gets the First and Last name of the user.
    """
    while True:
        user_input = input("Please enter your First and Last name..\n")
        name_list = user_input.split()
        if len(name_list) == 2:
        # Check that the input contains just a first and last name only
            if user_input.replace(" ", "").isalpha():
            # Check that the input contains only letters after removing any spaces
                return user_input
            else:
                print("Err: Please enter only letters.")
        else:
            print("Err: too many names given.")


def get_users_age():
    """
    Function gets the age of the user.
    """
    while True:
        user_input = input("Please enter your age.\n")
        if user_input.replace(" ", "").isdigit():
            # Check that the input contains only numbers after removing any spaces
            return user_input
        else:
            print("Err: Please enter only numbers.")


def validate_user(user):
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
    validate_user(user_name)


main()