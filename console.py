#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage
import json
from models.engine.file_storage import FileStorage


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
                        name_id = key.split('.')
                        if name_id == argv:
                            print("[{}] ({}) {}".
                                  format(argv[0], argv[1], value))
                            return
                    print("** no instance found **")
            except:
                pass

    def do_destroy(self, arg):
        """destroys the instance, but saves the changes in JSON file
        """
        argv = arg.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            store = storage.all()
            key = "{}.{}".format(argv[0], argv[1])
            print(store)
            if key in store:
                del store[key]
            print(store)
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
                            insta_str = "[{}] ({}) {}".format(name_id[0],
                                                              name_id[1], value)
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
