#!/usr/bin/python3
""" Class BaseModel defines all common attributes/methods for other classes """
import uuid
from datetime import datetime
import models


class BaseModel():
    """ Class for base model """

    def __init__(self, *args, **kwargs):
        """ Initialization """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """ Str format for references """
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Update with current date time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Dictionary containing all keys/values """
        dct = dict(self.__dict__)
        dct["__class__"] = self.__class__.__name__
        dct["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dct["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dct
