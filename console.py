#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '

    def emptyline(self):
        """doesn't do anything when type Enter
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def do_create(self, arg):
        """createsa new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_model = eval(argv[0])()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """prints representation of an object
        """
        argv = arg.split()
        input("arguments")
        print(argv)
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            try:
                load_dict = {}
                with open("file.json", "r") as f:
                    load_dict = json.load(f)
                    for key, value in load_dict.items():
                        input("key argum")
                        name_id = key.split('.')

                        print(name_id)

                        if name_id == argv:
                            print(value)
                            return
                    print("** no instance found *")
            except:
                pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
