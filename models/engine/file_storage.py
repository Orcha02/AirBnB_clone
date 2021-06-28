#!/usr/bin/python3
""" CLass FileStorage serializes instances to a JSON file and deserializes JSON file to instances """

import json
from models.base_model import BaseModel


class FileStorage:
    '''Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Return the dictionary '''
        return FileStorage.__objects

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id 
        '''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        obj_dict = {}      

        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as f:
            if FileStorage.__objects is not None:
                for key, val in FileStorage.__objects.items():
                    obj_dict[key] = val.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                for key, val in (json.load(f)).items():
                    val = eval(val["__class__"])(**val)
                    self.__objects[key] = val
        except FileNotFoundError:
            pass
