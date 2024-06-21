from django.db import models

# Create your models here.

# defining a class structure here and the object will be instanced in the views.py
class Destination: 
    id : int
    name: str
    desc: str
    img: str
    price: int
    offer : bool

