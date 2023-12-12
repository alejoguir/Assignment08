# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# AGuillen,12.09.2023,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
import data_classes as data


class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []
        self.employee_type = data.Employee

    def test_input_menu_choice(self):
        # Simulate user input '3' and check if the function returns '3'
        with patch('builtins.input', return_value='3'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '3')

    def test_input_employee_data(self):
        # Simulate user input for employee data
        with patch('builtins.input', side_effect=['John', 'Doe', '2012-05-02', 4]):
            employees = []
            employees = IO.input_employee_data(self.employee_data, self.employee_type)
            self.assertEqual(len(employees), 1)

            self.assertEqual(employees[0].first_name, 'John')
            self.assertEqual(employees[0].last_name, 'Doe')
            self.assertEqual(employees[0].review_date, '2012-05-02')
            self.assertEqual(employees[0].review_rating, 4)

        with patch('builtins.input', side_effect=['Alice', 'Smith', 'invalid', 2]):
            IO.input_employee_data(self.employee_data, self.employee_type)
            self.assertEqual(len(self.employee_data), 1)

if __name__ == "__main__":
    unittest.main()