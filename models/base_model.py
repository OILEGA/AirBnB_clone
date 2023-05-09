#!/usr/bin/python3
from models import storage
import uuid
from datetime import datetime


class BaseModel:
  """ """
  def __init__(self, *args, **kwargs):
    """ Initializing our base instance 
    *args: gives list of arguments
    
    

