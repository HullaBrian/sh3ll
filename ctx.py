

class ctx(object):
    """
    Object for passing the context parameters, flags, and values to a local command function
    """
    def __init__(self, parameters={}, flags={}):
        self.parameters = parameters
        self.flags = flags