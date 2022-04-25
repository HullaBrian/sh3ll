from .ctx import ctx
from sh3ll.PB import ProgressBar


class command(object):
    def __init__(self, function, name, aliases=[], help="No help given", category="", progress=None):
        self.function = function  # Function to call when command is executed
        self.name = name  # Command name. More for help menus
        self.aliases = aliases  # Other names the command goes by
        self.help = help  # Help dialogue
        self.category = category  # Command category for command classing
        self.progress = progress

        if progress is not None:
            self.progress_bar = ProgressBar(progress)
        else:
            self.progress_bar = None

    def execute(self, parameters):
        if self.progress_bar is not None:
            print()
        self.function(ctx(parameters, self.progress_bar))
