class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.used = []
        self.index = 0

    def __next__(self):
        if self.index == len(self.items):
            raise StopIteration
        if self.items[self.index] not in self.used:
            self.used.append(self.items[self.index])
            self.index += 1
            return self.items[self.index - 1]
        self.index += 1

    def __iter__(self):
        return self
