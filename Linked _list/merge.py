class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return self.data


class Linked_list:
    def __init__(self):
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.previous = self.dummy

    def append(self, data):
        new_node = Node(data)
        new_node.previous = self.dummy.previous
        new_node.next = self.dummy
        self.dummy.previous.next = new_node
        self.dummy.previous = new_node

    def size(self):
        temp = self.dummy.next
        size = 0
        while temp is not self.dummy:
            temp = temp.next
            size += 1
        return size

    def __str__(self):
        temp = self.dummy.next
        s = ''
        while temp is not self.dummy:
            s += str(temp)
            if temp.next is not self.dummy:
                s += ' '
            temp = temp.next
        return s


def merge(L1: Linked_list, L2: Linked_list):
    temp = L2.dummy.previous
    while temp is not L2.dummy:
        L1.append(temp.data)
        temp = temp.previous
    return L1


inp = input('Enter Input (L1,L2) : ').split()
l1 = inp[0].split('->')
l2 = inp[1].split('->')
L1, L2 = Linked_list(), Linked_list()
for i in l1:
    L1.append(i)
for i in l2:
    L2.append(i)
print("L1    :", L1)
print("L2    :", L2)
print("Merge :", merge(L1, L2))
