#!/usr/bin/python3
"""
BETA VERSION The console: contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
import models
import json


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    intro = 'Welcome to the Airbnb console\n'
    prompt = '(hbnb)'
    cstr = ['BaseModel', 'User']
    csob = [BaseModel, User]

    def do_create(self, class_name):
        """create a new instance of Base model"""
        if class_name == '':
            print("** class name missing **")
        elif class_name not in self.cstr:
            print("** class doesn't exist **")
        else:
            classin = class_name
            ob = self.csob[HBNBCommand.cstr.index(class_name)]()
            models.storage.new(ob)
            models.storage.save()
            print(ob.id)

    def do_show(self, wline):
        """ Prints string representation of an instance based on clsname.id"""

        path = 'file.json'
        dico = {}
        parse = wline.split(' ')

        if len(parse) == 1:
            if parse[0] == '':
                print("** class name missing **")
            elif parse[0] not in HBNBCommand.cstr:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            dico = models.storage.all()
            keyx = parse[0] + '.' + parse[1]
            if keyx in dico:
                print(dico[keyx])
            else:
                print("** no instance found **")

    def do_destroy(self, wline):
        """Deletes an instance based on the class name and id"""

        path = 'file.json'
        parse = wline.split(' ')
        if len(parse) == 1:
            if parse[0] == '':
                print("** class name missing **")
            elif parse[0] not in HBNBCommand.cstr:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            keyx = parse[0] + '.' + parse[1]
            if keyx in models.storage.all():
                del models.storage.all()[keyx]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, wline):
        """Prints all string representation of all instances"""

        l = []
        c = wline.split(' ')
        if c[0]:
            if c[0] not in HBNBCommand.cstr:
                print("** class doesn't exist **")
            else:
                for k in models.storage.all().keys():
                    if k.split('.')[0] == c[0]:
                        l.append(models.storage.all()[k])

        else:
            for k in models.storage.all().keys():
                l.append(models.storage.all()[k])
        if l:
            print([str(item) for item in l])
        l.clear()

    def do_update(self, wline):
        """Updates an instance based on the class name"""

        parse = wline.split(' ')
        if parse[0] == '':
            print("** class name missing **")
        elif parse[0] and parse[0] not in HBNBCommand.cstr:
            print("** class doesn't exist **")
        elif len(parse) == 1:
            print("** instance id missing **")
        elif parse[0] + '.' + parse[1] not in models.storage.all():
            print("** no instance found **")
        elif len(parse) == 2:
            print("** attribute name missing **")
        elif len(parse) == 3:
            print("** value missing **")
        else:
            k = parse[0] + '.' + parse[1]
            dct = models.storage.all()
            parse[3] = parse[3].strip("'")
            setattr(dct[k], parse[2], parse[3].strip('"'))
            models.storage.save()

    def do_EOF(self, line):
        """End of file"""
        print("ok bye!")

        return True

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
