#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)


print("-- Create a new object --")
Berghain = BaseModel()
Berghain.name = "techno"
Berghain.my_number = 14
Berghain.save()
print(Berghain)

