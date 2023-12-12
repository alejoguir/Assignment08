# ------------------------------------------------------------------------------- #
# Title: Application Classes Module
# # Description: A collection of processing classes for managing the application
# ChangeLog: (Who, When, What)
# AGuillen,12.04.2023,Created Script
# ------------------------------------------------------------------------------- #
import json
from json import JSONDecodeError


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    AGuillen,12.04.2023,Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list[object], employee_type: object):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        AGuillen,12.04.2023,Created function

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: a reference to the Employee class
        :return: list
        """
        # file: TextIO = None
        list_of_dictionary_data: list[object] = []
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type(employee['FirstName'], employee['LastName'], employee['ReviewDate'], employee['ReviewRating'])
                    employee_data.append(employee_object)
        except FileNotFoundError as e:
            file = open(file_name, 'w')
            json.dump(list_of_dictionary_data, file)
            raise JSONDecodeError("Text file not found, creating file since it doesn't exist")
        except JSONDecodeError as e:
            file = open(file_name, 'w')
            json.dump(list_of_dictionary_data, file)
            raise JSONDecodeError("JSON data in file isn\'t valid, resetting JSON file")
        except ValueError as e:
            file = open(file_name, 'w')
            json.dump(list_of_dictionary_data, file)
            raise ValueError("JSON data in file isn\'t valid, resetting JSON file")
        except Exception as e:
            raise e
        finally:
            if file.closed == False:
                file.close()
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list[object]):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        AGuillen,12.04.2023,Created function

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise TypeError("Please check the data file's read/write permission")
        except Exception:
            raise Exception("There was a non-specific error!")
        finally:
            if not file.closed:
                file.close()