# <img src="docs/readme-image.jpg" style="width: 40px;height:40px;"> WORKOUT LOG 

**Developer: Kieran Merrett**

💻 [Visit live website](https://workout-log.herokuapp.com/)

![Mockup image](docs/home-screenshot.png)

## About

This is a command-line version of a workout log and workout generator.

The aim is to build a place for a user to store weight logs to use when working out and be able to generate a workout for the user depending on how long the have available. Workouts are random each time dependant on time.

## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Generate a random workout for a user dependant on time
- Be able to log in/ register a new account.
- Log and update weights weights acheived in a previous workouts


### Site Owner Goals

- Create a log that is easy and clear to the user
- Ensure that users understand the purpose of the log
- Generate a workout each time that is always new for the users.
## User Experience

### Target Audience

Aimed towards people aged 16+ (recommended age for starting gym work outs), general gym enthusiasts looking for random workouts and people who like to track their workout weights

### User Requirements and Expectations

- A simple, error-free workout creation tool
- Straightforward navigation
- Log personalisation once registered
- Adjustable log record

### User Manual

<details><summary>Click here to view instructions</summary>

#### Main Menu
On the main menu, users are presented with an ASCII art rendering of the name 'Workout Log'. Below the welcome graphic there are a couple of options for user to select from.
Operation: Input a numeric value and press enter key.
1. Login / Register
2. Workout
3. Exit

At any point in the log, if the user inputs a number or text which does not correspond to the available option then they will be prompt to try again.

1. ####  Login / Register
Clicking the first option to login/register, you will then be asked to enter your first AND last name. If registered already, you must validate the email registered to the account and are then are taken to the 'user menu'.

If user is NOT registered, you will be asked to create a new profile, y/n?
If 'No' entered, then you will be returned to the main menu. If yes, you will first be asked your age, this must validate between 16-100. Following age, you will be asked your email and then to confirm it. Once These steps have all been passed with no error, you will be taken to the 'user menu'

#### User Menu
Once validated or after creating a new profile, you arrive at the user menu. Here are three options to choose from:
1. Workout
2. View your log
3. Exit

Selecting option 1 here to Workout, you will be asked how long you want to workout for, 15, 25, 45 or 60 minutes. Depending on your selection being 1-4, a random workout is generated giving x4 'warm up' exercises and increasing by 2 for each workout length, 6-10 'Main workout' exercises.

It is personalised using your user name. Following the workout being generated, you are returned to the 'user menu'

Clicking option 2 will take you to your personalised log, first it generates a full list of your exercises and the weights associated to each on, displayed in kg. 
You the are asked if you would like to adjust your log, y/n?

If no, you are returned to the user menu. 
If yes then you are asked which exercise you would like to adjust with prompt to enter the exercise, asked the new value and following updating your log, it asks if you would like to adjust another.

If no, your returned to the main menu. 
If yes, your log is regenerated for ease of viewing with all new values and prompted again to enter exercise/ new value. 

Selecting option 3, 'Exit' the user quits the workout log and exits the terminal.

2. ####  Workout
Clicking the second option to Workout, you will be asked how long you want to workout for, 15, 25, 45 or 60 minutes. Depending on your selection being 1-4, a random workout is generated giving x4 'warm up' exercises and increasing by 2 for each workout length, 4-10 'Main workout' exercises.

As you are NOT logged in or registered at this point, you are returned to the main menu.

3. #### Exit
Selecting option 3, 'Exit' the user quits the workout log and exits the terminal.

</details>

[Back to Table Of Contents](#table-of-contents)

## User Stories

### Users

1. I want to have clear options to select in the main menu
2. I want to be able to generate a workout quickly
3. I want to have different workouts each time
4. I want to be able to sign up/ login
5. I want to be able to view my weights log
6. I want to be able to adjust my workout log weight value stored

### Site Owner

7. I want users to have a positive experience whilst using the log
8. I want users to select options from the menus easily
9. I want user names and emails to be stored on Google Sheets
10. I want the user to get feedback on an incorrect input
11. I want data entry to be validated
12. I want the users to have an option to Exit the log

[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Flowchart

The following flowchart summarises the structure and logic of the application.

<details><summary>Flowchart</summary>
<img src="docs/flowchart.png">
</details>

## Technologies Used

### Languages

- [Python](https://www.python.org/) programming language for the logic of the program

### Frameworks & Tools

- [Miro.com](https://miro.com/app/dashboard/) was used to draw the flowchart
- [GitHub](https://github.com/) was used to store the project code
- [Google Cloud Platform](https://cloud.google.com/cloud-console/) was used to manage access and permissions for Google Services such as Google auth, sheets etc.
- [Google Sheets](https://www.google.co.uk/sheets/about/) was used to store user details, user log and exercises for user
- [PEP8](https://pep8ci.herokuapp.com/) used to validate my python code
- [Heroku](https://https://heroku.com/) was used to deploy the project into live environment
- [Gitpod Workspace](https://gitpod.io/workspaces) used to write the project code using Code Institute template

### Libraries

#### Python Libraries
- random - used to randomise the workout when generating
- re - used for random expression validation when getting user email address

#### Third Party Libraries
- [colorama](https://pypi.org/project/colorama/) - JUSTIFICATION: I used this to add color to the terminal. I marked warning/error information with color red and user feedback with blue and green.
- [gspread](https://docs.gspread.org/en/latest/) - JUSTIFICATION: I used gspread to add and manipulate data in my Google spreadsheet and to interact with Google API.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/) - JUSTIFICATION: module used to set up the authentification needed to access the Google API and connect my Service Account with the Credentials function. A creds.json file is created with all details the API needs to access the google account. In deployment to Render this information is stored in the config var section.

[Back to Table Of Contents](#table-of-contents)

## Features

### Main menu

- Provides user with graphic welcome message
- Gives user option to workout or signin / register
- User stories covered: 1, 2, 4, 8, 12
 
<details>
<summary>Main Menu</summary>
<img src="docs/features/main-menu.png">
</details>
<br>

### Workout
- Generate a workout for the user
- Workout suited to time specified
- Give variety in the workout
- User stories covered: 2, 3, 7
  
<details>
<summary>Workout - Main Menu</summary>
<img src="docs/features/main-workout.png">
</details>
<details>
<summary>Workout - User Menu</summary>
<img src="docs/features/user-workout.png">
</details>
<br>

### Exit
- Gives the user the option to exit the workout log completely
- Appearing in both the main menu and the user menu
- User stories covered: 7, 12

<details>
<summary>Exit - Main Menu</summary>
<img src="docs/features/main-exit.png">
</details>
<details>
<summary>Exit - User Menu</summary>
<img src="docs/features/user-exit.png">
</details>
<br>

### Login / Register
- This gives the user the chance to sign up or log into their personal workout log
- Their data is stored and validated with Google Sheets
- User stories covered: 9, 11

<details>
<summary>Sign up</summary>
<img src="docs/features/user-signup.png">
</details>
<details>
<summary>Login</summary>
<img src="docs/features/user-login.png">
</details>
<br>

### User Menu
- Once signed up or logged in, this menu is where the user can decide to view their log, generate a workout or exit
- User stories covered: 1, 2, 5, 8, 12

<details>
<summary>User Menu</summary>
<img src="docs/features/user-menu.png">
</details>
<br>

### View Log
- Here the user can view the currently stored information for their profile
- User stories covered: 5

<details>
<summary>User Log</summary>
<img src="docs/features/user-log.png">
</details>
<br>

### Adjust Log
- Here the usere is given the chance to adjust their current log information for a specific exercise
- User stories covered: 6, 7, 11

<details>
<summary>Adjust Log</summary>
<img src="docs/features/adjust-log.png">
</details>
<br>

### Error Handling
- Upon incorrect information input across the workout log, value errors and input errors are raised if necessary and feedback given towards the correct input required.
- User stories covered: 10, 11

<details>
<summary>Input Error</summary>
<img src="docs/features/input-error.png">
</details>
<details>
<summary>Yes/No Error</summary>
<img src="docs/features/yes-no-error.png">
</details>
<br>

[Back to Table Of Contents](#table-of-contents)
<br>

## Validation

[PEP8 Validation Service](https://pep8ci.herokuapp.com/) was used to varify python code requirements. All the code passes with no errors and no warnings to show.

<details><summary>PEP8 check for run.py</summary>
<img src="docs/validation/run-py-PEP8-validation.png">
</details>

<details><summary>PEP8 check for colors.py</summary>
<img src="docs/validation/colors-py-PEP8-validation.png">
</details>
<br>

## Testing

The testing approach is as follows:
1. Manual testing of user stories

### Manual Testing:

1. I want to have clear options to select in the main menu

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Main Menu | Load up the Program | Main menu to load up without any issues and display the workout log logo | Worked as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-1.png">
</details>
<br>


2. I want to be able to generate a workout quickly

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Workout | Select option 2 from the main menu, select a length of time to workout | Workout to be generated giving a different amount of workouts depending on time selected | worked as expected |
| User Menu | Select option 1 from the user menu, select a length of time to workout | Workout to be generated, attaching the users name and giving a different amount of workouts depending on time selected | worked as expected |

<details><summary>Main Menu Workout</summary>
<img src="docs/testing/user-story-2-a-1.png">
<img src="docs/testing/user-story-2-a-2.png">
<img src="docs/testing/user-story-2-a-3.png">
</details>
<details><summary>User Menu Workout</summary>
<img src="docs/testing/user-story-2-b-1.png">
<img src="docs/testing/user-story-2-b-2.png">
<img src="docs/testing/user-story-2-b-3.png">
<img src="docs/testing/user-story-2-b-4.png">
</details>
<br>


3. I want to have different workouts each time

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Workout | repeating the process of selecting a 15 minute workout three times | Each workout to be different to the last in both 'warm up' and 'main workout' exercises | worked as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-3-a.png">
<img src="docs/testing/user-story-3-b.png">
<img src="docs/testing/user-story-3-c.png">
</details>
<br>

4. I want to be able to sign up/ login

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Login / Register | Input my first and last name and worked through the following questions | A profile not to be under my name so asked to create new profile. Worked through the questions following and a new profile created. Arrive at the user menu | worked as expected |
| Login / Register | Input my first and last name | A profile under my name to be found and asked to confirm the email registered before continuing to the user menu | worked as expected |

<details><summary>Register</summary>
<img src="docs/testing/user-story-4-a-1.png">
<img src="docs/testing/user-story-4-a-2.png">
<img src="docs/testing/user-story-4-a-3.png">
</details>
<details><summary>Login</summary>
<img src="docs/testing/user-story-4-b-1.png">
<img src="docs/testing/user-story-4-b-2.png">
</details>
<br>

5. I want to be able to view my weights log

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| View Log | Once passing login'register, select option 2 from the user menu to view user log | Log to be displayed and to reference the users name to show this log is specific to this user | worked as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-5-a-1.png">
<img src="docs/testing/user-story-5-a-2.png">
<img src="docs/testing/user-story-5-a-3.png">
</details>
<br>

6. I want to be able to adjust my workout log weight value stored

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Adjust log | Once passing login'register, select option 2 from the user menu to view user log, then answer yes to the adjust log question, enter the name of the exercise i wish to adjust then its new value. Then i answered yes to the adjust again question to view updated log  | Input of exercise name to be matched and its new value to be updated, giving confirmation of exercise and new value. Updating when full log request next viewed | worked as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-6-a-1.png">
<img src="docs/testing/user-story-6-a-2.png">
<img src="docs/testing/user-story-6-a-3.png">
<img src="docs/testing/user-story-6-a-4.png">
<img src="docs/testing/user-story-6-a-5.png">
<img src="docs/testing/user-story-6-a-6.png">
</details>
<br>

7. I want users to have a positive experience whilst using the log

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Across all screens | Simple navigation through each menu | responses to input to be given without issues | worked as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-7-a-1.png">
<img src="docs/testing/user-story-7-a-2.png">
<img src="docs/testing/user-story-7-a-3.png">
</details>
<br>

8. I want users to select options from the menus easily

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Main Menu | Load up the main program and select an option | Be presented with a choice of options and an easy way to identify your choice | worked as expected |
| User Menu | Log into the main program and progress through to the user menu | Be presented with a choice of options and an easy way to identify your choice | worked as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-8-a.png">
<img src="docs/testing/user-story-8-b.png">
</details>

9. I want user names and emails to be stored on Google Sheets

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Login / Register | Sign up to the program and progress through the menus as a new user | profile to be created and my information to be stored when logging in next time | worked as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-9-a-1.png">
<img src="docs/testing/user-story-9-a-2.png">
<img src="docs/testing/user-story-9-a-3.png">
<img src="docs/testing/user-story-9-a-4.png">
</details>
<br>

10. I want the user to get feedback on an incorrect input

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| across all inputs | enter incorrect information which could potentialy be accepted or throw an error | Value error to be raised and asked again for your input | worked as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/user-story-10-a-1.png">
<img src="docs/testing/user-story-10-a-2.png">
<img src="docs/testing/user-story-10-a-3.png">
<img src="docs/testing/user-story-10-a-4.png">
<img src="docs/testing/user-story-10-a-5.png">
</details>
<br>

11. I want data entry to be validated

| **Feature** | **Action** | **Expected Result**| **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Login/regster | Attempt to sign in using a mixture of uppercase and lower case letters combined | Profile to be found and not asked to sign up to a new one | worked as expected |
| Adjust log | Attempt to adjust log using letters and numbers | Value error to be thrown and asked to input just numbers only | worked as expected |

<details><summary>Login/register</summary>
<img src="docs/testing/user-story-11-a-1.png">
<img src="docs/testing/user-story-11-a-2.png">
</details>
<details><summary>Adjust Log</summary>
<img src="docs/testing/user-story-11-b-1.png">
</details>
<br>

12. I want the users to have an option to Exit the log

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Main menu | From the main menu, select option 3 | expect the program to provide message giving feedback before exiting the program. No more further inputs affect the program | worked as expected |
| User menu | From the User menu, select option 3 | expect the program to provide message giving feedback before exiting the program. No more further inputs affect the program | worked as expected |

<details><summary>Main Menu</summary>
<img src="docs/testing/user-story-12-a-1.png">
<img src="docs/testing/user-story-12-a-2.png">
</details>
<details><summary>User Menu</summary>
<img src="docs/testing/user-story-12-b-1.png">
<img src="docs/testing/user-story-12-b-2.png"> 
</details>
<br>

[Back to Table Of Contents](#table-of-contents)

## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
|  |  |

## Deployment

### Heroku
This application has been deployed from GitHub to Heroku by following the steps:

1. 
2. 


### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Contents](#table-of-contents)

## Credits

### Images
- [Flaticon](https://www.flaticon.com/free-icon/connect_1707222) was used for the website favicon

### Code
- Code Institute - for git template IDE and "Love Sandwiches - Essentials Project" which helped me with connecting the Google Spreadsheet to my project.
- [ASCII Art Generator]() was used to create game title
- [gspread documentation](https://docs.gspread.org/en/latest/user-guide.html) explained how to obtain a specific value from the google spreadsheet
- Instructions how to print colored text from [this]()

## Acknowledgements
I would like to thank everyone who supported me in the development of this project:
- My mentor Mo for professional guidance, helpful feedback and words of encouragement whilst creating the project.
- Code Institute community on Slack for resources and support