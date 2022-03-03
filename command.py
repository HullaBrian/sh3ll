import exceptions


class command(object):
    def __init__(self, function, name, callName, aliases=[], flags=[], parameters=[], help="No help given"):
        self.function = function  # Function to call when command is executed
        self.name = name  # Command name. More for help menus
        self.callName = callName  # Actual word used to call the command
        self.aliases = aliases  # Other names the command goes by
        self.flags = flags  # Flags that the command takes
        self.parameters = parameters  # Parameters that the command takes
        self.help = help  # Help dialouge

    def execute(self, flags, parameters):
        if len(self.flags) > 0:
            for flag in self.flags:
                if flag not in flags:
                    print(f"~Command {self.name} recieved unexpected flag --{flag}")
                    raise exceptions.unexpectedFlag(self.name, flag)
        elif len(self.flags) == 0 and len(flags) != 0:
            print(f"~Command {self.name} does not take flags.")
        count = 0
        missing = []
        if len(list(parameters.keys())) == 0 and len(self.parameters) != 0:
            missing.append(self.parameters[self.parameters[0]])
        for x in list(self.parameters):
            flag = False
            for y in list(parameters.keys()):
                if x == y:
                    count += 1
                    flag = True
            if flag:
                missing.append(x)

        if count == len(self.parameters):
            return str(self.function(parameters=parameters))
        else:
            for missing_param in missing:
                parameters[missing_param] = ""
            return str(self.function(parameters=parameters))