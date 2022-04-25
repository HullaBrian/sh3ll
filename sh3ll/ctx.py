

class ctx(object):
    """
    Object for passing the context parameters, flags, and values to a local command function
    """
    def __init__(self, parameters=[], progress_bar=None):
        self.parameters = parameters
        self.progress_bar = progress_bar
