# AT-Project_1
Guvi, Capstone Project-1

## Overview:
This project is designed for automating the testing of a OrangeHRM web application using Python, Selenium WebDriver and Pytest. The focus is on verifying user login functionality and employee management operations such as adding, editing, and deleting employee records and utilizes Excel for data management.

## Table of Contents:
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Test Cases](#test-cases)
- [Running the Tests](#running-the-tests)
- [Test Data Configuration](#test-data-configuration)

## Features:
- __User Authentication Testing:__ Test the login functionality with valid and invalid credentials.
- __Employee Management:__ Tests functionalities for adding, editing, and deleting employee details.
- __Excel Integration:__ Read from and write test data to an Excel file for easy management and reporting.
- __Reusable Components:__ Common functions and data are abstracted into separate modules for better maintainability.
- __Dynamic Waits:__ Uses Explicit waits for web elements to ensure stability during testing.
- __Data-Driven Testing Framework:__ Utilizes Excel files for input data, allowing for flexible test execution with varying user credentials and employee details.
- __Automation Framework:__ Built using Selenium for browser automation and Pytest for test case management.

## Prerequisites:
- Python 3.x
- Required libraries:
  - selenium
  - pytest
  - openpyxl
  - webdriver-manager
 
## Installation:
To successfully set up and run the Selenium Automation Testing Project, follow these steps:

1. Ensure that you have Python 3.x installed on your machine. You can download it from _python.org_.

2. Familiarity with command-line interface (CLI) tools is recommended for executing commands.

3. Set Up a Virtual Environment (Optional but Recommended):
   - It's best practice to create a virtual environment to manage dependencies for your project:
     - Verify Python Virtual Environment: `Virtualenv --version`
     - Create Virtual Environment:  `virtualenv cd`
     - Activate Virtual Environment:  `Scripts\Activate`
     - Deactivate Virtual Environment: `Scripts\Deactivate`
       
4.  Install Required Libraries:
    - Install the necessary Python libraries using pip. The required libraries for this project include:
      - __Selenium :__ For web browser automation.
        Install Python Selenium Module: `pip install selenium`
      - __Pytest :__ For running test cases and managing test execution.
        `pip install pytest`
         Pytest Report: `pip install pytest-html`
      - __openpyxl :__ For reading and writing Excel files.
         `pip install selenium openpyxl`
      - __Webdriver-manager :__ To automatically manage browser drivers.
          Install WebDriver Manager Module: `pip install webdriver-manager`

## Project Structure: 
```
AT_Project_01/
├── Data/
│   └── WebData.py                # Contains test data and configuration.
├── Locators/
│   └── TestLocators.py            # Defines locators for web elements.
├── ExcelFunctions/
│   └── ExcelFunctions.py           # Functions for reading and writing Excel files.
├── Project01TestCases.py           # Contains test case implementations (main file).
├── TestCases/
│   ├── test_loginTestSuite.py      # Test suite for login tests.
│   └── test_suite_PIM.py           # Test suite for employee management tests.
├── common.py                       # Initializes common resources for tests.
└── test_data.xlsx                 # Excel file containing test data.
├── Reports/
│   ├── loginTC.html                # Pytest HTML Report for the Login test suite.
│   └── pimTC.html                  # Pytest HTML Report for the PIM test suite.
```

## Test Cases:
-  __Login Tests:__
   - __test_tc_login_01:__ Tests the login functionality using credentials from Excel and checks if the user is directed to the dashboard.
   - __test_tc_login_02:__ Another login test to validate login with different credentials and handles error messages.
     
- __Employee Management Tests:__
   - __test_TC_PIM_01:__ Tests adding a new employee and checks for a success message.
   - __test_TC_PIM_02:__ Tests editing an existing employee's details and verifies the updated message.
   - __test_TC_PIM_03:__ Tests deleting an employee and ensures the deletion is confirmed with a success message.

## Running the Tests:
- __To run all test cases:__
  - To execute all test cases in the project, navigate to the project directory and use the following command:	`pytest`
  -This command will automatically discover and run all test files that match the pattern **test_*.py**

- __Running Specific Tests:__
  - To run a specific test case, specify the test file and the test function. For example, to run the login test cases, use:
                  `pytest test_loginTestSuite.py`
  - To run a specific test within that file, use: `pytest test_loginTestSuite.py::test_tc_login_01`
  
- __Generate a Report:__
  -  To create an HTML report of the test results, you can use:
     ```
     pytest -v -s --capture=sys --html=Reports\loginTC.html test_loginTestSuite.py
     ```
     
- __Viewing Test Results:__
  - After running the tests, results will be displayed in the terminal. You will see the status of each test (passed, failed, etc.), along with any relevant output or error messages.
  - Check the output in the console for test results. Successful tests will also update the corresponding results in *test_data.xlsx*.
  - The pytest html report will be generated and saved in the Reports folder.

## Test Data Configuration:
- Ensure that the *test_data.xlsx* file is properly configured with the necessary test credentials and data for your tests to execute correctly.
- Check the output in the console for test results. Successful tests will also update the corresponding results in *test_data.xlsx*.






      










 



