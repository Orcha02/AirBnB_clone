#!/usr/bin/python3
import cmd
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import models

class HBNBCommand(cmd.Cmd):
    """" HBNBcommand class interpreter """

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
        except KeyError:
            print("** no instance found **")
            return
            

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
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
        """
        obj_lst = []
        args = shlex.split(args)
        if len(args) == 0:
            models.storage.reload()
            for i, obj in models.storage.all().items():
                obj_lst.append(obj.__str__())
            print(obj_lst)
            return
        try:
                eval(args[0])
        except NameError:
                print("** class doesn't exist **")
                return
        
        models.storage.reload()
        for i, obj in models.storage.all().items():
            if obj.__class__.__name__ == args[0]:
                obj_lst.append(obj.__str__())
        print(obj_lst)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
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
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
