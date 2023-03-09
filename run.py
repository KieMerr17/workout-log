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


def initial_question():
    """
    Ask the user what they would like to do
    """
    print("What would you like to do?")
    choices = "1) Login/Register\n2) Workout\n3) Exit\n"
    choice_selected = input(choices)
    separate_line()
    # Check if input is 1 or 2
    while choice_selected not in ("1", "2", "3"):
        print("Please choose an option:")
        choice_selected = input(choices)
        separate_line()

    if choice_selected == "1":
        user_name = get_users_name()
        validate_user(user_name)

    if choice_selected == "2":
        print("Generating workout...")
        separate_line()

    if choice_selected == "3":
        print("SEE YOU AGAIN...")
        exit()


def get_users_name():
    """
    Function gets the First and Last name of the user.
    Function checks it contains only a first and last name
    and the input data has only letters.
    the input it titled to avoid multiple entries before returning.
    """
    while True:
        user_input = input("Please enter your First and Last name...\n")
        name_list = user_input.split()
        if len(name_list) == 2:
            # Check that the input contains just a first and last name only
            if user_input.replace(" ", "").isalpha():
                # Check that the input contains only letters after removing
                # any spaces
                titled_input = user_input.title()
                USERS_NAME.append(titled_input)
                return titled_input
            else:
                print("Err: Please enter only letters.")
        else:
            print("Err: Incorrect number of names given.")


def get_users_age():
    """
    Function gets the age of the user.
    The function checks that the input contains only numbers and that
    the input age is between 16 - 100 years old.
    """
    while True:
        user_input = input("Please enter your age...\n")
        user_input = user_input.replace(" ", "")
        if user_input.isdigit():
            # Check that the input contains only numbers
            age = int(user_input)
            if age >= 16 and age <= 100:
                # Check that the input age is between 16 - 100
                return age
            else:
                print("Err: Age must be between 16 - 100.")
        else:
            print("Err: Please enter only numbers.")


def validate_user(user):
    """
    Function checks to see if users input name is already on
    the spreadsheet.
    If NOT then it appends the name to the sheet.
    """
    profiles_sheet = SHEET.worksheet('profiles')
    log_sheet = SHEET.worksheet('log')
    profiles_names = profiles_sheet.col_values(1)
    if user in profiles_names:
        print("\nLoading your profile...")
        separate_line()
        user_menu()
    else:
        user_age = get_users_age()
        profiles_sheet.append_row([user, user_age])
        log_sheet.append_row([user] + [0]*14)
        print("\n>> New profile created <<")
        separate_line()
        user_menu()


def separate_line():
    """
    Print '-' lines to separate messages
    """
    print(" ")
    print("- "*20)
    print(" ")


def user_menu():
    """
    Question to the user once validated
    """
    print("What would you like to do?")
    choices = "1) Workout\n2) View Log\n3) Exit\n"
    choice_selected = input(choices)
    # Check if input is 1 or 2
    while choice_selected not in ("1", "2", "3"):
        print("Please choose an option:")
        choice_selected = input(choices)

    if choice_selected == "1":
        print("\nGenerating workout...")
        separate_line()

    if choice_selected == "2":
        print("\nLoading your log...")
        separate_line()
        view_user_log()

    if choice_selected == "3":
        print("\nSEE YOU AGAIN...")
        separate_line()
        exit()


def view_user_log():
    """
    Generate current log history for the user logged in
    """
    name = "".join(USERS_NAME)  # convert USER_NAME to a string
    log_sheet = SHEET.worksheet('log')
    find_user = log_sheet.find(name, in_column=1)
    users_row = find_user.row
    users_log = log_sheet.row_values(users_row)  # current users log
    exercise = log_sheet.row_values(1)  # list of the exercise headings

    print(f"Workout Log for: {name}\n")
    user_data = {exercise[i]: users_log[i] for i in range(1, len(exercise))}
    # Create dictionary for exercise name and the users value

    print("\n"'\n'.join([f"{key}: {value}" for key, value in user_data.items()]))
    # Print Dictionary without '[]'
    separate_line()
    user_menu()


USERS_NAME = []
initial_question()
