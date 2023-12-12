# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# AGuillen,12.08.2023,Created Script
# ------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []
        self.employee_type = data.Employee

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "Ale", "LastName": "Gui", "ReviewDate": "2020-12-07", "ReviewRating": 3},
            {"FirstName": "Cyla", "LastName": "Phillips", "ReviewDate": "2023-10-12", "ReviewRating": 5},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        employee_data = FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, self.employee_type)

        # Assert that the student_data list contains the expected student objects
        self.assertEqual(len(self.employee_data), len(sample_data))

        for i in range(len(sample_data)):
            self.assertEqual(self.employee_data[i].first_name, sample_data[i]['FirstName'])
            self.assertEqual(self.employee_data[i].last_name, sample_data[i]['LastName'])
            self.assertEqual(self.employee_data[i].review_date, sample_data[i]['ReviewDate'])
            self.assertEqual(self.employee_data[i].review_rating, sample_data[i]['ReviewRating'])

    def test_write_employee_data_to_file(self):
        # Create some sample student objects
        sample_employees = [
            data.Employee("newJohn", "Doe", "2020-02-02", 4),
            data.Employee("newAlice", "Smith", "2021-01-01", 5),
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employees)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employees))

        for i in range(len(sample_employees)):
            self.assertEqual(file_data[0]['FirstName'], sample_employees[0].first_name)
            self.assertEqual(file_data[0]['LastName'], sample_employees[0].last_name)
            self.assertEqual(file_data[0]['ReviewDate'], sample_employees[0].review_date)
            self.assertEqual(file_data[0]['ReviewRating'], sample_employees[0].review_rating)


if __name__ == "__main__":
    unittest.main()
