#!/usr/bin/python3
import cmd
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """" HBNBcommand class interpreter """

    prompt = '(hbnb) '
    myClasses = ["BaseModel", "User", "Place", "State",
                 "City", "Amenity", "Review"]

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
        storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        obj_lst = []
        obj_dict = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in obj_dict.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_lst.append(val)
            else:
                obj_lst.append(val)
        print(obj_lst)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        pass

    def emptyline(self):
        """Print a new empty line"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
