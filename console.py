#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """" HBNBcommand class interpreter """

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """ Function of (End Of File) """
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        pass

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        pass

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        pass

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        pass

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