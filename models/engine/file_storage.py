#!/usr/bin/python3
""" CLass FileStorage serializes instances to a JSON file and deserializes JSON file to instances """

import json
import models

class FileStorage:
    '''Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Return the dictionary '''
        return self.__objects

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id 
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
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
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
