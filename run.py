import gspread
import random
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

print("__          __        _               _    ")
print("\ \        / /       | |             | |   ")
print(" \ \  /\  / /__  _ __| | _____  _   _| |_  ")
print("  \ \/  \/ / _ \| '__| |/ / _ \| | | | __| ")
print("   \  /\  / (_) | |  |   < (_) | |_| | |_  ")
print("    \/  \/_\___/|_|  |_|\_\___/ \__,_|\__| ")
print(" _                                         ")
print("| |                                        ")
print("| |     ___   __ _                         ")
print("| |    / _ \ / _` |                        ")
print("| |___| (_) | (_| |                        ")
print("|______\___/ \__, |                        ")
print("              __/ |                        ")
print("             |___/                         ")
print("                                           ")


def initial_question():
    """
    Ask the user what they would like to do
    """
    print("What would you like to do?")
    choices = "1) Login/Register\n2) Workout\n3) Exit\n"
    choice_selected = input(choices)
    separate_line()
    # Check if input is option 1 , 2 or 3
    while choice_selected not in ("1", "2", "3"):
        print("Err: Please choose an option:")
        choice_selected = input(choices)
        separate_line()

    if choice_selected == "1":
        user_name = get_users_name()
        validate_user(user_name)

    if choice_selected == "2":
        print("Ok, lets Workout!")
        separate_line()
        generate_workout()

    if choice_selected == "3":
        print("SEE YOU AGAIN...\n")
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
    choices = "1) Workout\n2) View Log\n3) Adjust Log\n4) Exit\n"
    choice_selected = input(choices)
    separate_line()
    # Check if input is 1, 2, 3 or 4
    while choice_selected not in ("1", "2", "3", "4"):
        print("Err: Please enter option 1, 2, 3 or 4")
        choice_selected = input(choices)
        separate_line()

    if choice_selected == "1":
        print("Ok, lets Workout!")
        separate_line()
        generate_workout()

    if choice_selected == "2":
        print("Loading your log...")
        separate_line()
        view_user_log()

    if choice_selected == "3":
        print("Lets first load your log...")
        separate_line()
        adjust_log()

    if choice_selected == "4":
        print("SEE YOU AGAIN...")
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
    # Create dictionary for exercise name and the users value
    user_data = {exercise[i]: users_log[i] for i in range(1, len(exercise))}

    # Print Dictionary without '[]' to the terminal
    print('\n'.join([f"{key}: {value}" for key, value in user_data.items()]))
    separate_line()
    return user_data


def generate_workout():
    """
    Generate a random workout using the information stored in the 
    exercises worksheet on Google Sheets
    """
    # Get the exercise data from the sheet
    exercise_sheet = SHEET.worksheet('exercises')
    
    time = time_question()
    if USERS_NAME:
        print(f"{time} minute workout for: {USERS_NAME[0]}\n")
    else:
        print(f"Please enjoy your {time} minute workout:\n")

    # Get the data from each column, ignoring the first row
    warmup_col = exercise_sheet.col_values(2)[1:]
    exercise_col = exercise_sheet.col_values(3)[1:]

    # Depending on time selected, reps/rest times given 
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
    print("\nWarm Up:")
    for i in random.sample(range(len(warmup_col)), k=4):
        print("- " + warmup_col[i])

    # Main Workout
    print("\nMain Workout:")
    for i in random.sample(range(len(exercise_col)), k):
        reps = random.choice(reps_data)
        print("- " + exercise_col[i] + "\n- " + str(reps) + "\n")
        reps_data.append(reps)
    
    if USERS_NAME:
        separate_line()
        user_menu()
    else:
        separate_line()
        initial_question()


def time_question():
    """
    Ask the question to the useruser how long they want to work out for
    """
    print("How long would you like to workout?")
    choices = "1) 15 minutes\n2) 25 minutes\n3) 45 minutes\n4) 60 minutes\n"
    choice_selected = input(choices)
    separate_line()
    # Check if input is option 1 , 2 , 3 or 4
    while choice_selected not in ("1", "2", "3", "4"):
        print("Please choose an option:")
        choice_selected = input(choices)
        separate_line()

    # Main workout
    if choice_selected == "1":
        print("You selected: 15 minutes")
        separate_line()
        return 15

    elif choice_selected == "2":
        print("You selected: 25 minutes")
        separate_line()
        return 25

    elif choice_selected == "3":
        print("You selected: 45 minutes")
        separate_line()
        return 45

    elif choice_selected == "4":
        print("You selected: 60 minutes")
        separate_line()
        return 60


def adjust_log():
    """
    give the user the option to adjust the number element of their
    user log, either increase or decrease it.
    """
    name = "".join(USERS_NAME)  # convert USER_NAME to a string
    log_sheet = SHEET.worksheet('log')
    find_user = log_sheet.find(name, in_column=1)
    users_row = find_user.row
    users_log = log_sheet.row_values(users_row)  # current users log
    exercise = log_sheet.row_values(1)  # list of the exercise headings

    users_log_info = view_user_log()
    selected_exercise = input("Which exercise shall we adjust?\n").title()

    #  Check if input data is in list of exercises
    while selected_exercise not in users_log_info.keys():
        print("\nErr: Exercise not recognized.")
        selected_exercise = input("Which exercise shall we adjust?\n").title()

    while True:
        #  Enter new value for the exercise
        new_value = input("Enter new value:\n")
        if new_value.isdigit():
            #  Add new value to user log and return new list
            users_log_info[selected_exercise] = new_value
            break
        else:
            print("\nErr: Please enter a number.")

    # Add to a variable the updated user log values in a Dictionary format.
    new_user_log = {exercise[i]: users_log[i] for i in range(1, len(exercise))}

    # Update users selected exercise
    new_user_log[selected_exercise] = users_log_info[selected_exercise]

    # Transfer over the new information to Google Sheets
    for i in range(1, len(exercise)):
        log_sheet.update_cell(users_row, i+1, new_user_log[exercise[i]])

    # Message saying which exercise has been updated and the new value
    print(f"\n{selected_exercise} has been updated to: {new_value}\n")

    # Ask if user would like to adjust another exercise
    adjust_again = input("Would you like to adjust another?\n").title()

    while adjust_again not in ("Yes", "No"):
        print("\nErr: Please enter Yes or No")
        adjust_again = input("Would you like to adjust another?\n").title()

    if adjust_again == "Yes":
        adjust_log()
    if adjust_again == "No":
        separate_line()
        user_menu()


USERS_NAME = []
initial_question()
