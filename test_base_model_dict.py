#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.nombre = "Holberton"
my_model.my_numero = 89
my_model.apellid = "Toribio"
print(f"my_model.id: {my_model.id}")
print(f"my_model: {my_model}")
print(f"my_model type: {type(my_model.created_at)}")
print("--")
my_model_json = my_model.to_dict()
print(f"my_model_json: {my_model_json}")
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
