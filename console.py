#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User
from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '
    class_list = {"BaseModel", "User", "State", "City", "Place",
                  "Amenity", "Review"}

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
        """creates a new instance of BaseModel,
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
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        """
        objects = storage.all()
        object_list = []
        if not arg:
            for key in objects:
                object_list.append(str(objects[key]))
            print(object_list)
            return
        argv = arg.split()
        if argv[0] in self.class_list:
            for key in objects:
                if key[0:len(argv[0])] == argv[0]:
                    object_list.append(str(objects[key]))
            print(object_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update instance attribute based on class name and id
        """
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

    def default(self, arg):
        """retrieve all instances of a class
        """
        count = 0
        object_list = []
        objects = storage.all()
        argv = arg.split(".")
        if argv[0] in self.class_list:
            if argv[1][0:4] == "show":
                i_d = argv[1][argv[1].index("(") + 1:argv[1].rindex(")")]
                if not i_d:
                    print("** instance id missing **")
                else:
                    key = argv[0] + "." + i_d
                    if key in objects:
                        print(objects[key])
                    else:
                        print("** no instance found **")
            if argv[1][0:7] == "destroy":
                i_d = argv[1][argv[1].index("(") + 1:argv[1].rindex(")")]
                if not i_d:
                    print("** instance id missing **")
                else:
                    key = argv[0] + "." + i_d
                    if key in objects:
                        del objects[key]
                    else:
                        print("** no instance found **")

            if argv[1][0:6] == "update":
                i_d = argv[1][argv[1].index("(") + 1:argv[1].rindex(")")]
                if not i_d:
                    print("** instance id missing **")
                else:
                    _id = i_d.split(", ")
                    print(_id)
                    _id[0] = _id[0].replace('\"', '')
                    key = argv[0] + "." + _id[0]
                    if type(_id[1]) is dict:
                        input("type")
                        print(type(_id[1]))
                        for keys, value in _id[1].items():
                            input("keys")
                            print(keys)
                            input("value")
                            print(value)
                            input("obj")
                            print(objects[key])
                            setattr(objects[key], keys, value)
                            storage.save()
                            return
                    i_d = i_d.replace('\"', '')
                    input("i_d if not")
                    print(i_d)

                    _id = i_d.split(", ")
                    input("_id split")
                    print(_id)
                    input("id's")
                    print(_id[0])
                    print(_id[2])
                    print(_id[1])

                    _id, attribute, value = _id
                    input("keys")
                    print(_id)
                    input("value")
                    print(value)
                    input("obj")
                    print(attribute)
                    if key in objects:
                        setattr(objects[key], attribute, value)
                        storage.save()
                    else:
                        print("** no instance found **")
            for key, value in objects.items():
                keys = key.split(".")
                if keys[0] == argv[0]:
                    count += 1
                    object_list.append("{}".format(value))
            if argv[1] == "all()":
                print("[" + ', '.join(map(str, object_list)) + "]")
            if argv[1] == "count()":
                print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
