import exceptions


class command(object):
    def __init__(self, function, name, callName, aliases=[], flags=[], parameters=[], declareVariables=False, requiresArgument=False, help="No help given"):
        self.function = function
        self.name = name
        self.callName = callName
        self.aliases = aliases
        self.flags = list(flags)
        self.parameters = parameters
        self.declareVariables = declareVariables
        self.requiresArgument = requiresArgument
        self.help = help

    def execute(self, flags, parameters):
        if len(self.flags) > 0:
            for flag in self.flags:
                if flag not in flags:
                    print(f"~Command {self.name} recieved unexpected flag --{flag}")
                    raise exceptions.unexpectedFlag(self.name, flag)
        elif len(self.flags) == 0 and len(flags) != 0:
            print(f"~Command {self.name} does not take flags.")
        elif len(self.flags) == 0 and len(flags) == 0:
            return str(self.function(parameters=parameters))
        else:
            return str(self.function(flags=flags, parameters=parameters))