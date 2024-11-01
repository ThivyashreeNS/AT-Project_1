"""test_suite_PIM.py"""

# Import pytest and shared resources for test cases.
import pytest
from common import get_test_case_instance,xlobj

# Test case for the first PIM functionality - To add a new employee
def test_TC_PIM_01():
    # Get test case instance.
    shree = get_test_case_instance()
    # Expected success message.
    test_msg = "Success Successfully Saved"
    # Check if the test case returns the expected message and writes to Excel
    assert shree.TC_PIM_01() == test_msg
    xlobj.write_data(4, 9, test_msg)
    # Close the driver.
    shree.close_driver()

# Test case for the second PIM functionality - Edit the employee details
def test_TC_PIM_02():
    shree = get_test_case_instance()
    updated_msg = "Successfully Updated"
    # Validate the test case result.
    assert shree.TC_PIM_02() == updated_msg
    # Write result to Excel.
    xlobj.write_data(5, 9, updated_msg)
    shree.close_driver()

# Test case for the second PIM functionality - Delete an employee
def test_TC_PIM_03():
    shree = get_test_case_instance()
    delete_msg = "Successfully Deleted"
    # Validate the test case result.
    assert shree.TC_PIM_03() == delete_msg
    xlobj.write_data(6, 9, delete_msg)
    shree.close_driver()