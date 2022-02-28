from difflib import SequenceMatcher
import inspect


class CLA(object):
    def __init__(self, prefix="CLA>"):
        self.prefix = prefix
        self.commands = []  # Implement a dictionary registry thingy
        self.helps = []

    def run(self):
        "TODO: Write ability to do --param value"
        help = False
        for command in self.commands:
            if command.name == "help":
                help = True

        while True:
            line = input(self.prefix).lower()
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
                            self.commands[self.commands.index(command)].execute(*args)
                            #print(self.commands[self.commands.index(command)])
                    except TypeError:
                        # print(f"Command '{self.commands[self.commands.index(command)].__name__}' missing required parameters.")
                        required_parameters = inspect.getargspec(self.commands[self.commands.index(command)].function)
                        pass
    
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


class command(object):
    def __init__(self, function, name, callName, aliases=[], requiresArgument=False, help="No help given"):
        self.function = function
        #self.params = params
        self.name = name
        self.callName = callName
        self.aliases = aliases
        self.requiresArgument = requiresArgument
        self.help = help

    def execute(self, params):
        self.function(*params)



app = CLA(">")

@app.command(name="test", callName="test", aliases=["test", "tst"], help="test command")
def test(e):
    print("Command 'test' executed.")
    print(e)


app.run()