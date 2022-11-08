class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        s = ''
        for i in self.items:
            s += str(i)
        return s


def prioCheck(op):
    if op in '+-':
        return 0
    elif op in '*/':
        return 1
    elif op in '^':
        return 2


def infixTopostfix(infix):
    infix_list = []
    infix_list.extend(infix)
    opStack = Stack()
    postfix = []
    for i in infix_list:
        if not opStack.isEmpty():
            if i in '+-':
                while not opStack.isEmpty() and opStack.peek() != '(' and prioCheck(opStack.peek()) >= prioCheck(i):
                    postfix.append(opStack.pop())
                opStack.push(i)
            elif i in '*/':
                while not opStack.isEmpty() and opStack.peek() != '(' and prioCheck(opStack.peek()) >= prioCheck(i):
                    postfix.append(opStack.pop())
                opStack.push(i)
            elif i == '^':
                while not opStack.isEmpty() and opStack.peek() != '(' and prioCheck(opStack.peek()) >= prioCheck(i):
                    postfix.append(opStack.pop())
                opStack.push(i)
            elif i == '(':
                opStack.push(i)
            elif i == ')':
                while not opStack.peek() == '(':
                    postfix.append(opStack.pop())
                else:
                    opStack.pop()
            else:
                postfix.append(i)
        else:
            if i in '+-*/^()':
                opStack.push(i)
            else:
                postfix.append(i)
    else:
        while not opStack.isEmpty():
            postfix.append(opStack.pop())
    s = ''.join(postfix)
    return s


inp = input('Enter Infix : ')
print(infixTopostfix(inp))
