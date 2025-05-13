#!/usr/bin/python3
"""Module that defines the Student class"""


class Student:
    """Class that defines a student.

    Attributes:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of strings representing attribute names

        Returns:
            dict: Dictionary containing the specified attributes
        """
        my_dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for ele in attrs:
                if ele in self.__dict__:
                    my_dict[ele] = self.__dict__[ele]
        return my_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing key/value
            pairs to replace attributes with
        """
        for key, value in json.items():
            setattr(self, key, value)
