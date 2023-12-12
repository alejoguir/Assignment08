# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# AGuillen,12.04.2023,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith", "2018-03-24", 3)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, "2018-03-24")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_review_date_type(self):  # Test the review_date validation
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "invalid_date", 4)

    def test_employee_review_rating_value(self):  # Test the review_rating validation
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "2021-10-12", "invalid_rating")

    def test_employee_str(self):
        employee = Employee("Eve", "Brown", "2023-07-28", 4)  # Tests the __str__() magic method
        self.assertEqual(str(employee), "Eve,Brown,2023-07-28,4")


if __name__ == '__main__':
    unittest.main()


