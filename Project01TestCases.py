"""Project01TestCases.py"""

# Import necessary modules from Selenium and other libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import TestLocators
from Data import WebData
from ExcelFunctions import ExcelFunctions


# Main test class inheriting WebData and TestLocators
class Project01TestCases(WebData, TestLocators):

    # Constructor for initializing the class
    def __init__(self):
        self.url = WebData().url
        # Initializing Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Set up an explicit wait for 10 seconds
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get(self.url)
        # Initialize ExcelFunctions for data handling
        self.xlobj = ExcelFunctions(WebData().excel_file, WebData().sheet_number)

    # Login method using credentials from Excel.
    def login(self, username_row, password_row):
        # Read username and password from Excel
        username = self.xlobj.read_data(username_row, 8)
        password = self.xlobj.read_data(password_row, 9)
        try:
            # Wait for the username & password field and input data, then click login.
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().username_name))).send_keys(username)
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().password_name))).send_keys(password)
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().login_button))).click()

            # Check for error message if the login was unsuccessful
            try:
                error_element = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().error_element)))
                # If the error element is visible, get the error text
                if error_element.is_displayed():
                    error_text = error_element.text
                    print("Login failed :", error_text)
                    return self.driver.current_url, error_text  # Return current URL and error text
            # Return any exceptions encountered
            except Exception as error:
                pass

            # Return current URL after successful login
            print("Login successful.")
            return self.driver.current_url, None
        # Print any login errors
        except Exception as error:
            print("Error during login:", error)
            return self.driver.current_url, error


    # Test case for first login scenario
    def tc_login_01(self):
        # Calls login with specific row numbers
        return self.login(2, 2)

    # Test case for second login scenario
    def tc_login_02(self):
        return self.login(3, 3)

    # Test case for adding a new employee
    def TC_PIM_01(self):

        # Using the defined login() method
        self.login(4, 4)

        try:
            # Navigate to PIM section
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().pim_text))).click()
            print("Navigated to PIM section")

            # Click the add button to add a new employee
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().add_button))).click()
            print("Clicked on Add button")

            # Input first name, middle name, and last name from WebData
            first = self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().first_name)))
            first.send_keys(WebData().firstname)
            print("Entered First Name")
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().middle_name))).send_keys(WebData().middlename)
            print("Entered Middle Name")
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().last_name))).send_keys(WebData().lastname)
            print("Entered Last Name")

            # add_photo_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().add_photo_btn)))
            # add_photo_button.click()
            # print("add photo clicked")
            # Wait for the file input element to be visible
            # self.driver.implicitly_wait(10)
            # add_photo = self.wait.until(EC.visibility_of_element_located((By.XPATH, TestLocators().photo_input)))
            # add_photo_button.send_keys(WebData().photo)
            # print("pic")

            # Get the employee ID after adding an employee
            employee_id_box = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().employee_id_box)))
            # Get employee ID value
            employee_id = employee_id_box.get_attribute("value")
            print(employee_id)
            # Write the employee ID to Excel file
            self.xlobj.write_data(4, 12, employee_id)
            # Click save button
            save = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().save_button)))
            save.click()

            # Wait for and retrieve the toast message confirming addition
            toast_msg = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, TestLocators().toast_add_msg)))
            # Combine toast messages into a single string
            save_toast_msg = " ".join(msg.text for msg in toast_msg).strip()
            print(save_toast_msg)
            # Return the combined message if it matches
            return save_toast_msg

        # Print any errors while adding an employee
        except Exception as error:
            print("Error while adding employee:", error)

    # Test case for editing employee details
    def TC_PIM_02(self):
        self.login(5, 5)
        try:
            # Navigate to PIM
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().pim_text))).click()
            # Search for the employee using the previously saved employee ID
            employee_id = self.xlobj.read_data(4, 12)
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().employee_id_box))).send_keys(employee_id)
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().search_button))).click()
            # Edit employee details
            self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().edit_button))).click()
            print("Clicked on Edit Button")
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().personal_details))).click()
            print("Clicked on Personal Details")

            # Enter driver license number
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().driver_license_number))).send_keys(WebData.license_number)
            print("Entered Driver License Number")

            # Wait for the gender radio button to be located
            gender_radio_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().gender_radio_btn)))
            # Scroll to gender radio button
            self.driver.execute_script("arguments[0].scrollIntoView();", gender_radio_btn)
            # print("Gender Radio Button is displayed:", gender_radio_btn.is_displayed())
            # print("Gender Radio Button is enabled:", gender_radio_btn.is_enabled())

            # Check if the radio button is selected and click if not
            if not gender_radio_btn.is_selected():
                # Use JavaScript to click
                self.driver.execute_script("arguments[0].click();", gender_radio_btn) # Click it if it's not selected
                print("Selected Gender Radio Button")
            else:
                print("Gender Radio Button is already selected")

            # Select nationality from dropdown
            # Open the dropdown
            dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().nationality_dropdown)))
            self.driver.execute_script("arguments[0].click();", dropdown)
            # Wait for options to become visible
            scroll = self.wait.until(EC.visibility_of_element_located((By.XPATH,TestLocators().nationality)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
            # Wait for options to become visible and select the desired option
            self.driver.execute_script("arguments[0].click();", scroll)
            print("Selected Nationality: Indian")

            # Save changes
            save = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().save_button)))
            save.click()

            # Wait for the Toast to be located and get the text of the toast message
            toast_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().toast_update)))
            update_toast_msg = toast_msg.text
            return update_toast_msg

        except Exception as error:
            print("Error while editing employee:", error)

    def TC_PIM_03(self):
        self.login(6, 6)
        try:
            # Navigate to PIM
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().pim_text))).click()
            # Search for employee
            employee_id = self.xlobj.read_data(4, 12)
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().employee_id_box))).send_keys(employee_id)
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().search_button))).click()
            # Delete employee details
            self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().trash_button))).click()
            delete_employee = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().delete_button)))
            delete_employee.click()
            # Wait and retrieves the text of the toast message to confirm the deletion.
            toast_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().toast_delete_msg)))
            delete_toast_msg = toast_msg.text
            return delete_toast_msg

        except Exception as error:
            print("Error while deleting employee:", error)

    # Closes the browser driver and quits the session.
    def close_driver(self):
        self.driver.quit()

