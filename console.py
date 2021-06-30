#!/usr/bin/python3
""" Contains the entry point of the command interpreter. """

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models


class HBNBCommand(cmd.Cmd):
    """ HBNBcommand class interpreter """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ Function of (End Of File) """
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        Example (replace - with spaces):
        create-name_of_class
        """
        try:
            args = shlex.split(args)
            if args == []:
                print("** class name missing **")
                return
            else:
                expresion = args[0]
                new_ins = eval(expresion)()
                new_ins.save()
                print(new_ins.id)
                return
        except:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        Example (replace - with spaces):
        show-name_of_class-id_object
        """
        args = shlex.split(args)
        key = ""
        obj_dict = storage.all()
        if args == []:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = str(args[0]) + "." + str(args[1])
        try:
            print(obj_dict[key])
            return
        except KeyError:
            print("** no instance found **")
            return

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        Example (replace - with spaces):
        destroy-name_of_class-id_object
        """
        args = shlex.split(args)
        key = ""
        obj_dict = storage.all()
        if args == []:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = str(args[0]) + "." + str(args[1])
        try:
            del(obj_dict[key])
        except KeyError:
            print("** no instance found **")
            return
        storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name
        If you need all the instances created only
        with the sentence 'all'.
        If you need the instances created from a specific class,
        then type 'all name_of_class'
        """
        obj_lst = []
        args = shlex.split(args)
        if len(args) == 0:
            models.storage.reload()
            for key, val in models.storage.all().items():
                obj_lst.append(val.__str__())
            print(obj_lst)
            return
        try:
                eval(args[0])
        except NameError:
                print("** class doesn't exist **")
                return
        models.storage.reload()
        for key, val in models.storage.all().items():
            if val.__class__.__name__ == args[0]:
                obj_lst.append(val.__str__())
        print(obj_lst)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        Example (replace - with spaces):
        update-name_of_class-id_object-attribute-value_attribute
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        args = shlex.split(args)
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = str(args[0]) + "." + str(args[1])
        obj_dict = storage.all()
        try:
            obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        setattr(obj_dict[key], args[2], args[3])
        storage.save()

    def emptyline(self):
        """Print a new empty line"""
        return

    def do_count(self, args):
        '''Counts the number of instances.'''
        count = 0
        args = args.split()
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        for key in obj_dict.values():
            if args[0] == key.__class__.__name__:
                count += 1
        print(count)

    def default(self, args):
        ''' Default execute the functions. '''
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", args[0])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
