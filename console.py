#!/usr/bin/python3
"""Console for AirBnB"""

from models import storage
from models.base_model import BaseModel
import cmd
import json

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "
    class_list = ['BaseModel']

    def do_greet(self, line):
        print("hello")

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_create(self, arg):
        """ creates a new instance
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            new_model = eval(argv[0])()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """prints string representation based on class name and id
        """
        a_dict = {}
        input("open")
        with open("file.json", "r", encoding="utf-8") as f:
            a_dict = json.load(f)
            print(a_dict)
        input("after open")

        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist**")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            try:
                load_dict = {}
                with open("file.json", r) as f:
                    print(f)
            except:
                pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
