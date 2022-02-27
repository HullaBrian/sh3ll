

from difflib import SequenceMatcher


class CLA(object):
    def __init__(self, prefix="CLA>"):
        self.prefix = prefix
        self.commands = []

    def run(self):
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
                if command.__name__ != inputted_command:
                    highestSimiliarity = 0
                    for command in self.commands:
                        similarity = SequenceMatcher(None, command.__name__, inputted_command).ratio()
                        if similarity > highestSimiliarity:
                            highestSimiliarity = SequenceMatcher(None, command.__name__, inputted_command).ratio()
                            mostSimilarCommandId = command.__name__
                    print(f"Command not recongnized.\nDid you mean: '{mostSimilarCommandId}'?")
                else:
                    try:
                        self.commands[self.commands.index(command)](*args)
                    except TypeError:
                        print(f"Command '{self.commands[self.commands.index(command)].__name__}' missing required parameters.")
            
    def command(self, name, help):
        def wrap(function):
            self.commands.append(function)
            # print(f"[CLA]: Registered command '{name}'")
            def wrapped_function(*args):
                return function(*args)
            return wrapped_function
        return wrap



app = CLA(">")

@app.command(name="help", help="Help command")
def help(e):
    print("Command 'help' executed.")
    print(e)


app.run()