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
- [unittest](https://docs.python.org/3/library/unittest.html) - used to carry out testing on single units in validation.py file

#### Third Party Libraries
- [colorama](https://pypi.org/project/colorama/) - JUSTIFICATION: I used this to add color to the terminal. I marked warning/error information with color red and user feedback with blue and green.
- [gspread](https://docs.gspread.org/en/latest/) - JUSTIFICATION: I used gspread to add and manipulate data in my Google spreadsheet and to interact with Google API.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/) - JUSTIFICATION: module used to set up the authentification needed to access the Google API and connect my Service Account with the Credentials function. A creds.json file is created with all details the API needs to access the google account. In deployment to Render this information is stored in the config var section.

[Back to Table Of Contents](#table-of-contents)

## Features

### Main menu

- 
- 
- 
 
<details>
    <summary></summary>

![](docs/)
</details>

### 
- 
- 
- 
  
<details>
    <summary></summary>

![](docs/)
</details>

### 
- 
- 

<details>
    <summary></summary>

![](docs/)
</details>

### 
- 
- 

[Back to Table Of Contents](#table-of-contents)

## Validation

[PEP8 Validation Service](https://pep8ci.herokuapp.com/) was used to varify python code requirements. All the code passes with no errors and no warnings to show.

<details><summary>PEP8 check for run.py</summary>
<img src="docs/validation/run-py-PEP8-validation.png">
</details>

<details><summary>PEP8 check for colors.py</summary>
<img src="docs/validation/colors-py-PEP8-validation.png">
</details>

## Testing

The testing approach is as follows:
1. Manual testing of user stories

### Manual Testing
<details><summary></summary>

1. 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
|  |  |  |  |

<details><summary></summary>
<img src="docs/">
</details>

2. 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
|  |  |  |  |

<details><summary></summary>
<img src="docs/">
</details>

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