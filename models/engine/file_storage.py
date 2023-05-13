#!/usr/bin/python3
import json
from models import base_model

class FileStorage():
    """ a class that serializes json and deserializes json file 
    to instances. We are also creating a private instance that is 
    a string and a path to the json file """
    
    __file_path = "file.json"
    __objects = {}

def all(self):
    return self.__objects

def new(self, obj):
    key = f"{obj.__class.__.__name__}.{obj.id}"
    self.__objects[key] = obj
    
    """ opening the file to enable us save ojects to json file """    
def save(self):
    with open(self.__file_path, "w", encoding="utf-8") as f:
        dc = {k : val.to_dict() for k, val in self.__objects.items()}
        json.dump(dc, f) #converting to json string; k= key

def reload(self):
    try:
        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            for o in obj_dict.values():
                class_name = o["__class__"]
                del o["__class__"]
                self.new(eval(f"base_model.{class_name}")(**o))

    except FileNotFoundError:
        return


