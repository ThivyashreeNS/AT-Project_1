"""
Locators.py
This is a Python file for Web Locators
"""
class TestLocators:
    # Login locators
    username_name = "username"
    password_name = "password"
    login_button = "//button[@type='submit']"
    error_element = "//p[text() = 'Invalid credentials']"
    logout_button = "//a[text()='Logout']"

    # PIM locators
    pim_text = "PIM"
    employee_id_box = "//label[text()='Employee Id']/following::input[@class='oxd-input oxd-input--active']"
    save_button = "//button[@type='submit']"

    # Locators of add employee
    add_button = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    first_name = "firstName"
    middle_name = "middleName"
    last_name = "lastName"
    add_photo_btn = "//i[@class='oxd-icon bi-plus']"
    photo_input = "//input[@type='file']/following-sibling::div[@class='oxd-file-div oxd-file-div--active']"
    toast_add_msg = "//div[@class='oxd-toast-content oxd-toast-content--success']//p"
    add_photo = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button/i"

    # Locators of edit employee
    search_button = "//button[@type='submit' and text()=' Search ']"
    edit_button = "(//button[@type='button']/following::i[@class='oxd-icon bi-pencil-fill'])[1]"
    personal_details = "Personal Details"
    nationality_dropdown = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]"
    nationality = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]"
    driver_license_number = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"
    gender_radio_btn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label"
    toast_update = "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[2]"

    # Locators of delete employee
    trash_button = "(//button[@type='button']/following::i[@class='oxd-icon bi-trash'])[1]"
    toast_delete_msg = "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[2]"
    delete_button = "//button[@type='button' and text()=' Yes, Delete ']"
