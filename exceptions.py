

class unexpectedFlag(Exception):
    def __init__(self, commandName, flag):
        super().__init__(f"{commandName} recieved an unexpected flag {flag}")