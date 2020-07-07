class stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        return self.list.pop()

    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False

    def peek(self):
        return self.list[-1]