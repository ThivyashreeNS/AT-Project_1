"""common.py"""
# Import classes from their modules
from Project01TestCases import Project01TestCases
from Data import WebData
from ExcelFunctions import ExcelFunctions

# Initialize common resources
excel_file = WebData().excel_file
sheet_number = WebData().sheet_number
# Creates an instance of ExcelFunctions which handles Excel operations.
xlobj = ExcelFunctions(excel_file, sheet_number)

# Defines a function that returns an instance of the Project01TestCases class.
def get_test_case_instance():
    return Project01TestCases()
