class ProgressBar(object):
    def __init__(self, pos=()):
        if len(pos) == 2:
            self.start, self.end = pos[0], pos[1]
            self.position = 0

    def __str__(self):
        percent = (self.position / float(self.end - self.start)) * 100
        bar = '█' * int(percent) + '-' * (100 - int(percent))
        # print(f"\r|{bar}| {percent:.2f}%", end="\r")
        return f"\rProgress: |{bar}| {percent:.2f}%"

    def progress(self, value):
        if self.position <= self.end:
            self.position += value

            if self.position == self.end - self.start:
                print(self, flush=True)
            else:
                print(self, end="\r", flush=True)
