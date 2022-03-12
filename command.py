from ctx import ctx

class command(object):
    def __init__(self, function, name, callName, aliases=[], parameters=[], help="No help given"):
        self.function = function  # Function to call when command is executed
        self.name = name  # Command name. More for help menus
        self.callName = callName  # Actual word used to call the command
        self.aliases = aliases  # Other names the command goes by
        self.parameters = parameters  # Parameters that the command takes
        self.help = help  # Help dialouge

    def execute(self, parameters):
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
            self.function(ctx(parameters))
        else:
            for missing_param in missing:
                parameters[missing_param] = ""
            self.function(ctx(parameters))