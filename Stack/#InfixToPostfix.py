#InfixToPostfix
class Stack:
    def __init__(self,L=None):
        if L is None:
            self.l = []
        else:
            self.l = L
    
    def pop(self):
        return self.l.pop()

    def push(self,data):
        self.l.append(data)

    def peek(self):
        return self.l[-1]

    def size(self):
        return len(self.l)

    def isEmpty(self):
        return self.l == []

    def __str__(self):
        return str(self.l)

def priority(op):
    if op in '+-':
        return 1
    elif op in '*/':
        return 2
    elif op in ')':
        return 3
    else:
        return 0


inp = input('Enter Input : ')




