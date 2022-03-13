from difflib import SequenceMatcher
from command import command


class CLA(object):
    def __init__(self, prefix="CLA>"):
        self.prefix = prefix
        self.commands = []
        """
        Param: -variable value
        """

    def run(self):
        help = False
        for command in self.commands:
            if command.name == "help":
                help = True

        while True:
            try:
                line = input(self.prefix).lower()
            except KeyboardInterrupt:
                exit()
            inputted_command = line.split()[0]

            # Parse command into command and arguments
            args = []
            tmp = line.split()[1:]
            count = 0
            for arg in range(len(tmp)):
                if count == 0:
                    if tmp[arg][0] == "'":
                        for arg2 in range(len(tmp[arg+1:])):
                            if tmp[arg+1+arg2][-1] == "'":
                                args.append(''.join([s.strip("'") for s in tmp[arg:arg+arg2+2]]))
                                count = len(tmp[arg:arg+arg2+1])
                    else:
                        if tmp[arg][-1] != "'":
                            args.append(tmp[arg])
                else:
                    count -= 1
            

            cmds = [cmd.name for cmd in self.commands]
            if inputted_command != "help":
                try:
                    command_index = cmds.index(inputted_command)
                    try:
                        self.commands[command_index].execute(args)
                    except KeyError:
                        print("Missing required parameters!")
                        flag = True
                except ValueError:
                    flag = False
                    for command in self.commands:
                        if inputted_command in command.aliases:
                            try:
                                self.commands[self.commands.index(command)].execute(args)
                            except KeyError:
                                print("Missing required parameters!")
                            flag = True
                    if not flag:
                        highestSimiliarity = 0
                        mostSimilarCommandId = -1
                        for command in self.commands:
                            similarity = SequenceMatcher(None, command.callName, inputted_command).ratio()
                            if similarity > highestSimiliarity:
                                highestSimiliarity = SequenceMatcher(None, command.callName, inputted_command).ratio()
                                mostSimilarCommandId = command.callName
                        print(f"Command not recognized.\nDid you mean: '{mostSimilarCommandId}'?")
            else:
                self.help()


    def help(self):
        print("~help\tDisplays this menu.")
        for command in self.commands:
            print(f"~{command.name}\t{command.help}")



    def command(self, name="Unknown command", callName="Uknown command", aliases=[], help="No help given"):
        def wrap(function):
            self.commands.append(command(function, name=name, callName=callName, aliases=aliases, help=help))
            # print(f"[CLA]: Registered command '{name}'")
            def wrapped_function(*args):
                return function(*args)
            return wrapped_function
        return wrap
    
    def comand_catagory(self):
        pass