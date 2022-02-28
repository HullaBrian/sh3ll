

from tokenize import Name
from typing import Type


class command(object):
    def __init__(self, function, name, callName, aliases=[], flags=[], parameters=[], declareVariables=False, requiresArgument=False, help="No help given"):
        self.function = function
        self.name = name
        self.callName = callName
        self.aliases = aliases
        self.flags = flags
        self.parameters = parameters
        self.declareVariables = declareVariables
        self.requiresArgument = requiresArgument
        self.help = help

    def execute(self, flags, parameters):
        try:
            self.function(flags=flags, parameters=parameters)
        except TypeError:
            print("oof")
            self.function(*parameters)