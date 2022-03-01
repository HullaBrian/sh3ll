from difflib import SequenceMatcher
import inspect
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
        "TODO: Write ability to do --param value"
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
            #print(flags)
            #print(parameters)

            for command in self.commands:
                if command.name != inputted_command:
                    if inputted_command == "help" and not help:
                            self.help()
                            continue
                    highestSimiliarity = 0
                    mostSimilarCommandId = -1
                    for command in self.commands:
                        similarity = SequenceMatcher(None, command.name, inputted_command).ratio()
                        if similarity > highestSimiliarity:
                            highestSimiliarity = SequenceMatcher(None, command.name, inputted_command).ratio()
                            mostSimilarCommandId = command.name
                    print(f"Command not recongnized.\nDid you mean: '{mostSimilarCommandId}'?")
                else:
                    try:
                        # print(help)
                        if inputted_command == "help" and not help:
                            self.help()
                        else:
                            print(args)
                            try:
                                print(self.commands[self.commands.index(command)].execute(flags, parameters))
                            except exceptions.unexpectedFlag:
                                print(f"Command {self.commands[self.commands.index(command)]} recieved unexpected flag.")
                    except TypeError:
                        # print(f"Command '{self.commands[self.commands.index(command)].__name__}' missing required parameters.")
                        required_parameters = str(inspect.signature(self.commands[self.commands.index(command)].function)).replace(")", "").replace("(", "").replace(",", "").split(",")
                        print("Required parameters:", required_parameters)

    def help(self):
        print("~help\tDisplays this menu.")
        for command in self.commands:
            print(f"~{command.name}\t{command.help}")



    def command(self, name="Unknown command", callName="Uknown command", aliases=[], flags=[], parameters=[], declareVariables=False, help="No help given"):
        def wrap(function):
            self.commands.append(command(function, name=name, callName=callName, aliases=aliases, flags=flags, parameters=parameters, declareVariables=declareVariables, help=help))
            # print(f"[CLA]: Registered command '{name}'")
            def wrapped_function(*args):
                return function(*args)
            return wrapped_function
        return wrap


app = CLA("dp>")

@app.command(name="test", callName="test", aliases=["test", "tst"], flags=[], parameters=["e"], declareVariables=False, help="test command")
def test(**kwargs):
    print("Command 'test' executed.")
    # Don't have to use this if you don't want to. This is simply to catch errors
    try:
        parameters = kwargs["parameters"]
    except KeyError:
        parameters = {}
    try:
        flags = kwargs["flags"]
    except KeyError:
        flags = {}

    e = parameters["e"]

    return e 


app.run()