# __init__.py

__version__ = "1.2.2"  # Be sure to update version in setup.py as well

from difflib import SequenceMatcher
from sh3ll.command import command
from art import tprint


class IS(object):
    def __init__(self, name="", font="", prefix="CLA>"):
        self.name = name
        self.font = font
        self.prefix = prefix
        self.commands = []
        self.categories = []
        """
        Param: -variable value
        """

    def run(self):
        if self.font != "":
            tprint(self.name, font=self.font)
        else:
            tprint(self.name)

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
                        for arg2 in range(len(tmp[arg + 1:])):
                            if tmp[arg + 1 + arg2][-1] == "'":
                                args.append(''.join([s.strip("'") for s in tmp[arg:arg + arg2 + 2]]))
                                count = len(tmp[arg:arg + arg2 + 1])
                    else:
                        if tmp[arg][-1] != "'":
                            args.append(tmp[arg])
                else:
                    count -= 1

            cmds = [cmd.name for cmd in self.commands]
            categories = [cmd.category for cmd in self.commands]

            aliases = {}
            for command in self.commands:
                aliases[command.name] = command.aliases

            if inputted_command != "help" and inputted_command != "exit" and inputted_command != "q":
                if inputted_command in cmds and self.commands[cmds.index(inputted_command)].category == "":
                    self.commands[cmds.index(inputted_command)].execute(args)
                elif inputted_command in categories:
                    if line.split()[1] in cmds:
                        if self.commands[cmds.index(line.split()[1])].category == line.split()[0]:
                            self.commands[cmds.index(line.split()[1])].execute(args[1:])
                    else:
                        for command in self.commands:
                            if line.split()[1] in command.aliases:
                                command.execute(args[1:])
                else:
                    highestSimilarity = 0
                    mostSimilarCommand = ""
                    mostSimilarCommandCategory = ""

                    for command in self.commands:
                        similarity = SequenceMatcher(None, command.name, inputted_command).ratio()
                        if similarity > highestSimilarity:
                            highestSimilarity = SequenceMatcher(None, command.name, inputted_command).ratio()
                            mostSimilarCommand = command.name
                            mostSimilarCommandCategory = command.category

                    print(f"Command not recognized.\nDid you mean: '{mostSimilarCommandCategory} {mostSimilarCommand}'?")
            else:
                self.help() if inputted_command == "help" else exit()

    def help(self):
        print("help\tDisplays this menu")
        print("exit OR q\tExits the program")
        for command in self.commands:
            if command.category == "":
                print(f"{command.name}\t{command.help}")
        print()

        for category in self.categories:
            if category != "":
                print(f"\"{category}\" Commands:\n" + ("-" * (len(category) + 12)))
                cmds = []
                for command in self.commands:
                    if command.category == category:
                        cmds.append(command)

                longest_name = max([len(cmd.name) for cmd in cmds])
                longest_aliases = max([len(str(cmd.aliases)) for cmd in cmds])
                longest_help = max([len(cmd.help) for cmd in cmds])

                print("\tCommand" + (" " * (abs((len(category) + 1 + longest_name) - 7) + 4)) + "Aliases" + (
                            " " * (abs(longest_aliases - 7) + 4)) + "Help" + " " * (abs(longest_help - 4) + 4))
                print("\t" + ("-" * 7) + (" " * (abs((len(category) + 1 + longest_name) - 7) + 4)) + ("-" * 8) + (
                            " " * (abs(longest_aliases - 8) + 4)) + ("-" * 4))

                for command in cmds:
                    if abs(longest_name - len(command.name)) == 0:
                        print(f"\t{category} {command.name}" + (" " * (abs((len(category) + 1 + longest_name) - (
                                    len(category) + len(command.name) + 1)) + 4)), end="")
                    else:
                        print(f"\t{category} {command.name}" + (" " * (
                                    abs((len(category) + 1 + longest_name) - len(f"{category} {command.name}")) + 4)),
                              end="")
                    if abs(longest_aliases - len(str(command.aliases))) == 0:
                        print(f"{command.aliases}    ", end="")
                    else:
                        print(f"{command.aliases}" + (" " * (abs(longest_aliases - len(str(command.aliases))) + 4)),
                              end="")
                    print(f"{command.help}" + (" " * abs(longest_help - len(command.help))))
                print()

    def command(self, name="Unknown command", aliases=[], help="No help given", category="", progress=()):
        def wrap(function):
            if category not in self.categories:
                self.categories.append(category)  # Auto register cats
            self.commands.append(command(function, name=name, aliases=aliases, help=help, category=category, progress=progress))

            def wrapped_function(*args):
                return function(*args)

            return wrapped_function

        return wrap