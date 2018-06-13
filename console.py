#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '
    class_list = {"BaseModel", "User"}

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
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            new_model = eval(argv[0])()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """prints representation of an object
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = argv[0] + "." + argv[1]
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """destroys the instance, but saves the changes in JSON file
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            store = storage.all()
            key = "{}.{}".format(argv[0], argv[1])
            if key in store:
                del store[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        """
        argv = arg.split()
        if len(argv) < 2:
            try:
                load_dict = {}
                list_of_all = []
                insta_str = ""
                with open("file.json", "r") as f:
                    load_dict = json.load(f)
                for key, value in load_dict.items():
                    name_id = key.split('.')
                    if len(argv) == 1:
                        if name_id[0] == argv[0]:
                            insta_str = "[{}] ({}) {}".format(
                                name_id[0], name_id[1], value)
                            list_of_all.append(insta_str)
                        else:
                            print("** class doesn't exist **")
                            return
                    else:
                        insta_str = "[{}] ({}) {}".format(name_id[0],
                                                          name_id[1], value)
                        list_of_all.append(insta_str)
                print(list_of_all)
                return
            except:
                pass

    def do_update(self, arg):
        """update instance attribute based on class name and id
        """
        #argv = arg.split()
        argv = shlex.split(arg)
        if len(argv) < 5:
            if len(argv) == 0:
                print("** class name missing **")
            elif argv[0] not in self.class_list:
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print("** instance id missing **")
            elif len(argv) == 2:
                print("** attribute name missing **")
            elif len(argv) == 3:
                print("** value missing **")
            else:
                store = storage.all()
                key = "{}.{}".format(argv[0], argv[1])
                if key in store:
                    setattr(store[key], argv[2], argv[3])
                    storage.save()
                else:
                    print("** no instance found **")
                    #storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
