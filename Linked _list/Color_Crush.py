class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class Linked_list:
    def __init__(self, data=None):
        self.dummy = Node()
        self.size = 0

    def getNode(self, index):
        temp = self.dummy.next
        for i in range(index):
            temp = temp.next  # get Node at specify index

        return temp.data

    def append(self, data):
        new_node = Node(data)
        if self.dummy.next == None:  # if no node in linked list
            self.dummy.next = new_node  # dummy -> new_node
            new_node.previous = self.dummy  # dummy -> <- new_node
            self.dummy.previous = new_node  # new_node <- dummy -> <- new_node
            # new_node-> <- dummy -> <- new_node so new_node is head &  tail
            new_node.next = self.dummy
            self.size += 1
        else:
            temp = self.dummy.next
            while temp.next != self.dummy:
                temp = temp.next  # get last Node
            else:
                temp.next = new_node  # last node -> new_node
                new_node.previous = temp  # last node -> <- new_node
                self.dummy.previous = new_node  # new_node <- dummy -> head
                new_node.next = self.dummy  # new_node -> <- dummy -> head
                self.size += 1

    def insert(self, index, data):
        new_node = Node(data)
        temp = self.dummy.next
        if index <= self.size and index >= 0:
            for i in range(index):
                temp = temp.next  # get Node at specify index
            if index == 0:
                if self.size == 0:
                    new_prev = self.dummy  # new_prev = dummy
                    new_next = self.dummy  # new_next = dummy
                    self.dummy.previous = new_node  # new_node <- dummy
                else:
                    new_prev = self.dummy  # new_prev = dummy
                    new_next = self.dummy.next  # new_next = dummy->head
                new_next.previous = new_node
                new_node.previous = new_prev  # dummy <- new_node
                new_node.next = new_next  # new_node -> dummy
                self.dummy.next = new_node  # dummy -> new_node so new_node become head node

            elif index == self.size and index > 0:
                new_prev = self.dummy.previous  # new_prev = last node <- dummy
                new_next = self.dummy  # new_next = None <- last node <- dummy
                new_prev.next = new_node
                new_node.previous = new_prev  # last node-> <- new_node
                new_node.next = new_next  # last node-> <- new_node ->None
                self.dummy.previous = new_node  # new_node <- dummy so new_node become last node

            else:
                new_prev = temp.previous
                new_next = temp
                new_node.previous = new_prev
                new_node.next = new_next

        elif index > self.size and index > 0:  # do like index == self.size
            new_prev = self.dummy.previous  # new_prev = last node <- dummy
            new_next = self.dummy.previous.next  # new_next = None <- last node <- dummy
            new_prev.next = new_node
            new_node.previous = new_prev  # last node-> <- new_node
            new_node.next = new_next  # last node-> <- new_node ->None
            self.dummy.previous = new_node  # new_node <- dummy so new_node = last node

        elif index < 0:
            for i in range(self.size + index):
                temp = temp.next  # get Node at specify index
            if index <= -self.size:
                new_prev = self.dummy  # new_prev = dummy
                new_next = self.dummy.next  # new_next = dummy -> head node
                new_next.previous = new_node
                new_node.previous = new_prev  # dummy <- new_node
                new_node.next = new_next  # new_node -> head node
                self.dummy.next = new_node  # dummy -> new_node so new_node become head node
            else:
                new_prev = temp.previous
                new_next = temp
                new_node.previous = new_prev
                new_node.next = new_next

        self.size += 1

    def remove(self, data):  # remove first data that value == specify data in parameter
        temp = self.dummy.next
        value = None
        while temp.data != data and temp != self.dummy:
            temp = temp.next
        else:
            if temp == self.dummy:
                pass
            else:
                prev = temp.previous
                next = temp.next
                prev.next = next
                next.previous = prev
                value = temp.data
                self.size -= 1
        return value

    def __str__(self):
        s = ''
        temp = self.dummy.next
        while temp.next != self.dummy:
            s += str(temp.data)
            if temp.next != self.dummy:
                s += '->'
            temp = temp.next
        else:
            s += str(temp.data)
        return s


inp = input('Enter Input : ').split()
list = Linked_list()
for data in inp:
    list.append(data)

color = list.dummy.next
combo = 0
while color != list.dummy:
    if color.next.data == color.data and color.next.next.data == color.data:
        combo += 1
        for i in range(3):
            list.remove(color.data)
            color = color.next
        color = list.dummy.next
    else:
        color = color.next

print(list.size)
s = list.dummy.previous
temp = ''
while s != list.dummy:
    temp += str(s.data)
    s = s.previous

if temp == '':
    print('Empty')
else:
    print(temp)

if combo >= 2:
    print(f'Combo : {combo} ! ! !')
