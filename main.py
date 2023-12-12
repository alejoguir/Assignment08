# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# AGuillen,12.04.2023,Created Script
# ------------------------------------------------------------------------------------------------- #

import processing_classes as proc
import presentation_classes as pres
import data_classes as data

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''

# Beginning of the main body of this script
try:
    employees = proc.FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=data.Employee)  # Note this is the class name (ignore the warning)
except Exception as e:
    pres.IO.output_error_messages("Got an exception reading from file", e)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees, employee_type=data.Employee)  # Note class name (ignore the warning)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
