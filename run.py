"""
Import python 'Random Expression Library
for use in validating email address input
"""
import re
import random
import gspread
from google.oauth2.service_account import Credentials
from colors import Color as Col

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

print(Col.BLUE + r"__          __        _               _    ")
print(Col.BLUE + r"\ \        / /       | |             | |   ")
print(Col.BLUE + r" \ \  /\  / /__  _ __| | _____  _   _| |_  ")
print(Col.BLUE + r"  \ \/  \/ / _ \| '__| |/ / _ \| | | | __| ")
print(Col.BLUE + r"   \  /\  / (_) | |  |   < (_) | |_| | |_ ")
print(Col.BLUE + r"    \/  \/_\___/|_|  |_|\_\___/ \__,_|\__|")
print(Col.YELLOW + r" _")
print(Col.YELLOW + r"| |")
print(Col.YELLOW + r"| |     ___   __ _")
print(Col.YELLOW + r"| |    / _ \ / _` |")
print(Col.YELLOW + r"| |___| (_) | (_| |")
print(Col.YELLOW + r"|______\___/ \__, |")
print(Col.YELLOW + r"              __/ |")
print(Col.YELLOW + r"             |___/")
print("\n")

# Google Sheet information used by more than one function
profiles_sheet = SHEET.worksheet('profiles')
log_sheet = SHEET.worksheet('log')


def initial_question():
    """
    Ask the user what they would like to do
    Check if input is option 1 , 2 or 3
    Cary out functions dependant on selection
    """
    print("What would you like to do?")
    choices = "1) Login / Register\n2) Workout\n3) Exit\n"
    choice_selected = input(choices)
    separate_line()

    while choice_selected not in ("1", "2", "3"):
        print(Col.RED + "Err: Please choose an option:")
        choice_selected = input(choices)
        separate_line()

    if choice_selected == "1":
        user_name = get_users_name()
        validate_user(user_name)

    if choice_selected == "2":
        print(Col.GREEN + "Ok, lets Workout!")
        separate_line()
        time = time_question()
        generate_workout(time, USERS_NAME)

    if choice_selected == "3":
        print(Col.BLUE + "SEE YOU AGAIN...")
        separate_line()
        exit()


def get_users_name():
    """
    Function gets the First and Last name of the user
    Function checks it contains only a first and last name
    and the input data has only letters.
    the input it titled to avoid multiple entries before returning.
    Value error if incorrect information given
    """
    while True:
        try:
            user_input = input("Please enter your First and Last name...\n")
            name_list = user_input.split()

            if len(name_list) != 2:
                raise ValueError("Incorrect number of names given.")

            if not user_input.replace(" ", "").isalpha():
                raise ValueError("Please enter only letters.")

            titled_input = " ".join(name_list).title().rstrip()
            USERS_NAME.clear()
            USERS_NAME.append(titled_input)
            print(Col.GREEN + "\nLooking for your profile...\n")
            return titled_input

        except ValueError as err_msg:
            print(Col.RED + "\nErr: " + str(err_msg))


def get_users_age():
    """
    Function gets the age of the user.
    The function checks that the input contains only numbers and that
    the input age is between 16 - 100 years old.
    Errors for incorrect information
    """
    while True:
        user_input = input("Please enter your age...\n")
        user_input = user_input.replace(" ", "")

        if user_input.isdigit():
            age = int(user_input)
            if age >= 16 and age <= 100:
                return age
            else:
                print(Col.RED + "Err: Age must be between 16 - 100.")
        else:
            print(Col.RED + "Err: Please enter only numbers.")


def get_users_email():
    """
    Function verifies that the input is a valid email address.
    Check that confirmed email matches the given email
    If it doesnt match then a value error is raised
    Value error if incorrect data
    """
    while True:
        try:
            user_input = input("Enter your email address: \n").replace(" ", "")
            adj_input = user_input.capitalize()

            if not re.match(r"[^@]+@[^@]+\.[^@]+", adj_input):
                raise ValueError("Invalid email address entered.")

            confirm_email = input("Confirm email address: \n").replace(" ", "")
            adj_confirm = confirm_email.capitalize()

            if adj_input == adj_confirm:
                return adj_confirm
            else:
                raise ValueError("Email address didn't match.")

        except ValueError as err_msg:
            print(Col.RED + f"\nErr: {str(err_msg)}")


def validate_user(user):
    """
    Function checks to see if users input name is already on
    the spreadsheet.
    if user found get user to varify email address
    If NOT then it asks if they want to set up new profile
    then appends the name, email and age to the sheet.
    Value error for incorrect input
    """
    profiles_names = profiles_sheet.col_values(1)

    if user in profiles_names:
        find_user = profiles_sheet.find(user, in_column=1)
        users_row = find_user.row
        users_log = profiles_sheet.row_values(users_row)
        stored_email = users_log[1:]

        while True:
            try:
                varify_email = input("Varify your email address..\n")
                adj_input = varify_email.replace(" ", "").capitalize()

                if adj_input in (stored_email):
                    separate_line()
                    user_menu()

                if adj_input == "Exit":
                    separate_line()
                    initial_question()
                else:
                    raise ValueError("Varify email or 'Exit'")

            except ValueError as err_msg:
                print(Col.RED + "\nErr: " + str(err_msg))
    else:
        create_new_profile(user)


def create_new_profile(user):
    """
    Question to create a new profile using the input
    and username given from the user
    append the given information to Google SHEETS pages:
    - Profiles
    - Logs
    """
    new_profile = input("Do you want to create a new profile?\n").title()
    answer = yes_no_question(new_profile)

    if answer == "Yes":
        print(Col.BLUE + "\nCreating profile...\n")
        # Ask user age
        user_age = get_users_age()
        print(Col.BLUE + "\nAdding your age...\n")
        # Ask user email
        user_email = get_users_email()
        print(Col.BLUE + "\nAdding your email...\n")
        # Add profile to SHEETS
        profiles_sheet.append_row([user, user_email, user_age])
        log_sheet.append_row([user] + [0]*14)
        separate_line()
        print(Col.GREEN + ">> New profile created <<")
        separate_line()
        user_menu()

    if answer == "No":
        USERS_NAME.clear()
        separate_line()
        initial_question()


def separate_line():
    """
    Print '-' lines to separate messages
    """
    print(" ")
    print(Col.YELLOW + "- "*20)
    print(" ")


def user_menu():
    """
    Question to the user once validated.
    error for incorrect option input
    """
    print("What would you like to do?")
    choices = "1) Workout\n2) View Your Log\n3) Exit\n"
    choice_selected = input(choices)
    separate_line()

    user = USERS_NAME

    while choice_selected not in ("1", "2", "3"):
        print(Col.RED + "Err: Please enter option 1, 2 or 3")
        choice_selected = input(choices)
        separate_line()

    if choice_selected == "1":
        print(Col.GREEN + "Ok, lets Workout!")
        separate_line()
        time = time_question()
        generate_workout(time, user)

    if choice_selected == "2":
        print(Col.GREEN + "Loading your log...")
        separate_line()
        adjust_log(user)

    if choice_selected == "3":
        print(Col.BLUE + "SEE YOU AGAIN...")
        separate_line()
        exit()


def view_user_log(user):
    """
    Generate current log history for the user logged in
    """
    user = "".join(USERS_NAME)  # convert USER_NAME to a string
    find_user = log_sheet.find(user, in_column=1)
    users_row = find_user.row
    users_log = log_sheet.row_values(users_row)  # users current log
    exercise = log_sheet.row_values(1)  # list of the exercise headings

    print("Workout Log for: " + Col.GREEN + f"{user}\n")

    # Create dictionary for exercise name and the users value
    user_data = {exercise[i]: users_log[i] for i in range(1, len(exercise))}

    # Print Dictionary without '[]' to the terminal
    print("Weight in: Kg\n")
    print('\n'.join([f"{key}: {value}" for key, value in user_data.items()]))
    separate_line()
    return user_data


def generate_workout(time, user):
    """
    Generate a random workout using the information stored in the
    exercises worksheet on Google Sheets for specified time
    if USER then append users name to the workout heading
    exit to relevant menu
    """
    exercise_sheet = SHEET.worksheet('exercises')

    if user:
        print(f"{time} minute workout for: " + Col.GREEN + f"{user[0]}\n")
    else:
        print("Please enjoy your: " + Col.GREEN + f"{time} minute workout\n")

    # Get the data from each column, ignoring the first row
    warmup_col = exercise_sheet.col_values(2)[1:]
    exercise_col = exercise_sheet.col_values(3)[1:]

    if time == 15:
        reps_data = exercise_sheet.col_values(4)[1:3]
        k = 4
    elif time == 25:
        reps_data = exercise_sheet.col_values(4)[1:4]
        k = 6
    elif time == 45:
        reps_data = exercise_sheet.col_values(4)[1:5]
        k = 8
    elif time == 60:
        reps_data = exercise_sheet.col_values(4)[1:6]
        k = 10

    # Warm up
    print(Col.YELLOW + "\nWarm Up:")
    for i in random.sample(range(len(warmup_col)), k=4):
        print("- " + warmup_col[i])

    # Main Workout
    print(Col.YELLOW + "\nMain Workout:")
    for i in random.sample(range(len(exercise_col)), k):
        reps = random.choice(reps_data)
        print("- " + exercise_col[i] + "\n- " + str(reps) + "\n")
        reps_data.append(reps)

    if user:
        separate_line()
        user_menu()
    else:
        separate_line()
        initial_question()


def time_question():
    """
    Ask the question to the useruser how long they want to work out for
    error for incorrect input
    """
    print("How long would you like to workout?")
    choices = "1) 15 minutes\n2) 25 minutes\n3) 45 minutes\n4) 60 minutes\n"
    choice_selected = input(choices)
    separate_line()

    while choice_selected not in ("1", "2", "3", "4"):
        print(Col.RED + "Err: Please choose an option:")
        choice_selected = input(choices)
        separate_line()

    if choice_selected == "1":
        print("You selected: " + Col.GREEN + "15 minutes")
        separate_line()
        return 15

    elif choice_selected == "2":
        print("You selected: " + Col.GREEN + "25 minutes")
        separate_line()
        return 25

    elif choice_selected == "3":
        print("You selected: " + Col.GREEN + "30 minutes")
        separate_line()
        return 45

    elif choice_selected == "4":
        print("You selected: " + Col.GREEN + "60 minutes")
        separate_line()
        return 60


def adjust_log(user):
    """
    give the user the option to adjust the number element of their
    user log, after viewing log, either increase or decrease it.
    if no, return to menu
    """
    user = "".join(USERS_NAME)  # convert USER_NAME to a string

    find_user = log_sheet.find(user, in_column=1)
    users_row = find_user.row
    users_log = log_sheet.row_values(users_row)  # current users log
    exercise = log_sheet.row_values(1)  # list of the exercise headings

    users_log_info = view_user_log(user)

    adjust_log_question = input("Would you like to adjust your log?\n").title()
    answer = yes_no_question(adjust_log_question)

    if answer == "Yes":
        separate_line()
        adjust_exercise(users_log_info, exercise, users_log, users_row)

    if answer == "No":
        separate_line()
        user_menu()


def adjust_exercise(users_log_info, exercise, users_log, users_row):
    """
    Function to get adjustment for the new value of the exercise and post it to
    Google Sheets.
    error if exercise not it list of exercises
    Then questions user if they would like to adjust again, if not return to
    user menu.
    """
    user = "".join(USERS_NAME)  # convert USER_NAME to a string
    selected_exercise = input("Which exercise shall we adjust?\n").title()

    if selected_exercise == "Exit":
        separate_line()
        user_menu()

    while selected_exercise not in users_log_info.keys():
        print(Col.RED + "\nErr: Exercise not recognized.")
        selected_exercise = input("Enter exercise or Exit to return\n").title()

        if selected_exercise == "Exit":
            separate_line()
            user_menu()

    while True:
        new_value = input("Enter new value:\n")

        if new_value.isdigit():
            #  Add new value to user log
            users_log_info[selected_exercise] = new_value
            break
        else:
            print(Col.RED + "\nErr: Please enter a number.")

    # Create dictionary for workout log
    new_user_log = {exercise[i]: users_log[i] for i in range(1, len(exercise))}
    # Update dictionary exercise with new value
    new_user_log[selected_exercise] = users_log_info[selected_exercise]
    # Update Google Sheets
    for i in range(1, len(exercise)):
        log_sheet.update_cell(users_row, i+1, new_user_log[exercise[i]])

    separate_line()
    print(Col.GREEN+f"{selected_exercise} has been updated to: {new_value}")
    separate_line()

    adjust_another = input("Would you like to adjust another?\n").title()
    answer = yes_no_question(adjust_another)

    if answer == "Yes":
        separate_line()
        view_user_log(user)
        adjust_exercise(users_log_info, exercise, users_log, users_row)

    if answer == "No":
        separate_line()
        user_menu()


def yes_no_question(user_input):
    """
    Returns a value of either Yes or No
    Value error if incorrect input
    """
    while True:
        try:
            if user_input.title() not in ("Yes", "No"):
                raise ValueError("Please enter Yes or No")
            else:
                return user_input.title()

        except ValueError as err:
            print(Col.RED + f"Err: {err}")
            user_input = input("").title()


USERS_NAME = []
initial_question()
