#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel():
    
    def __init__(self, *args, **kwargs):
        """ Initializing our base instances
        of id, created_at and updated_at
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ using the str to enable us print our instance and return a string """
        return f"({self.__class__.__name__}) ({self.id}) {self.__dict__}"

    def save(self):
        """ updates to realtime anytime a change is made """ 
        self.updated_at = datetime.now()

    def to_dict(self):
        """ creating and updating a copy of our origial dictionary """
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        return copy_dict



