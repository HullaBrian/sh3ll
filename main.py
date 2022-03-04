from difflib import SequenceMatcher
from command import command
import exceptions


class CLA(object):
    def __init__(self, prefix="CLA>"):
        self.prefix = prefix
        self.commands = []
        """
        Flag: --flag
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
            
            flags = []
            parameters = {}
            for arg in range(0, len(args)):
                if args[arg][:2] == "--":
                    flags.append(args[arg][2:])
                elif args[arg][:1] == "-":
                    parameters[args[arg][1:]] = args[arg + 1]

            for command in self.commands:
                if command.callName != inputted_command:
                    if inputted_command == "help" and not help:
                        self.help()
                        break
                    cmds = [cmd.callName for cmd in self.commands]
                    if inputted_command not in cmds:
                        highestSimiliarity = 0
                        mostSimilarCommandId = -1
                        for command in self.commands:
                            similarity = SequenceMatcher(None, command.callName, inputted_command).ratio()
                            if similarity > highestSimiliarity:
                                highestSimiliarity = SequenceMatcher(None, command.callName, inputted_command).ratio()
                                mostSimilarCommandId = command.callName
                        print(f"Command not recognized.\nDid you mean: '{mostSimilarCommandId}'?")
                        break
                else:
                    try:
                        if inputted_command == "help" and not help:
                            self.help()
                        else:
                            try:
                                self.commands[self.commands.index(command)].execute(flags, parameters)
                            except exceptions.unexpectedFlag:
                                print(f"Command {self.commands[self.commands.index(command)]} recieved unexpected flag.")
                    except TypeError:
                        # print(f"Command '{self.commands[self.commands.index(command)].__name__}' missing required parameters.")
                        # required_parameters = str(inspect.signature(self.commands[self.commands.index(command)].function)).replace(")", "").replace("(", "").replace(",", "").split(",")
                        print("Missing required parameters")

    def help(self, params=[]):
        print("~help\tDisplays this menu.")
        for command in self.commands:
            print(f"~{command.name}\t{command.help}")



    def command(self, name="Unknown command", callName="Uknown command", aliases=[], flags=[], parameters=[], help="No help given"):
        def wrap(function):
            self.commands.append(command(function, name=name, callName=callName, aliases=aliases, flags=flags, parameters=parameters, help=help))
            # print(f"[CLA]: Registered command '{name}'")
            def wrapped_function(*args):
                return function(*args)
            return wrapped_function
        return wrap