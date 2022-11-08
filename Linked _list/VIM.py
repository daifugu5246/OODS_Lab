class Node:
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.next = next
        self.previous = previous


class Linked_list:
    def __init__(self, data=None):
        self.cursor = Node('|')
        self.dummy = Node(None, self.cursor, self.cursor)
        self.cursor.previous = self.dummy
        self.cursor.next = self.dummy
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.cursor
        new_node.previous = self.cursor.previous
        self.cursor.previous.next = new_node
        self.cursor.previous = new_node

    def left(self):
        if self.cursor.previous is self.dummy:
            return
        self.cursor.data, self.cursor.previous.data = self.cursor.previous.data, self.cursor.data
        self.cursor = self.cursor.previous

    def right(self):
        if self.cursor.next is self.dummy:
            return
        self.cursor.data, self.cursor.next.data = self.cursor.next.data, self.cursor.data
        self.cursor = self.cursor.next

    def back(self):
        if self.cursor.previous is self.dummy:
            return
        self.cursor.previous = self.cursor.previous.previous
        self.cursor.previous.next = self.cursor

    def delete(self):
        if self.cursor.next is self.dummy:
            return
        self.cursor.next = self.cursor.next.next
        self.cursor.next.previous = self.cursor

    def __str__(self):
        s = ''
        temp = self.dummy.next
        while temp.next != self.dummy:
            s += str(temp.data)
            if temp.next != self.dummy:
                s += ' '
            temp = temp.next
        else:
            s += str(temp.data)
        return s


inp = input('Enter Input : ').split(',')
list = Linked_list()
cursor = Node('|')
for data in inp:
    if data[0] == 'I':
        word = data.split()[1]
        list.insert(word)
    elif data[0] == 'L':
        list.left()
    elif data[0] == 'R':
        list.right()
    elif data[0] == 'B':
        list.back()
    elif data[0] == 'D':
        list.delete()


print(list)
