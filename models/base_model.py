#!/usr/bin/python3
""" Class BaseModel defines all common attributes/methods for other classes """


class BaseModel:
    """ Class for base model """

    def __init__(self):
        """ Initialization """
        self.id =
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Str format """
        return "[{}] ({}) {}"

    def save(self):
        """ Update with current date time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Dictionary containing all keys/values """
