class Stack:
    def __init__(self, L=None):
        if L is None:
            self.l = []
        else:
            self.l = L

    def push(self, data):
        self.l.append(data)

    def pop(self):
        return self.l.pop()

    def peek(self):
        return self.l[-1]

    def isEmpty(self):
        return self.l == []

    def size(self):
        return len(self.l)

    def __str__(self):
        return str(self.l)