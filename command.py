from ctx import ctx

class command(object):
    def __init__(self, function, name, callName, aliases=[], help="No help given"):
        self.function = function  # Function to call when command is executed
        self.name = name  # Command name. More for help menus
        self.callName = callName  # Actual word used to call the command
        self.aliases = aliases  # Other names the command goes by
        self.help = help  # Help dialouge

    def execute(self, parameters):
        self.function(ctx(parameters))