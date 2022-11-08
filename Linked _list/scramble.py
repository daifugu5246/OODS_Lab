class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Linked_list:
    def __init__(self):
        self.dummy = Node()
        self.last = self.dummy
        self.last.next = self.dummy.next
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        self.last.next = new_node
        new_node.next = self.dummy
        self.last = new_node
        self.size += 1

    def riffle(self, pc):
        a = 0
        temp = self.dummy
        if int((pc/100)*self.size) > int(self.size/2):
            a = self.size - int((pc/100)*self.size)
        else:
            a = int((pc/100)*self.size)
        for i in range(int((pc/100)*self.size)):
            temp = temp.next
        pt1 = self.dummy.next
        pt2 = temp.next
        stop = temp.next
        for i in range(a):
            next1, next2 = pt1.next, pt2.next
            pt1.next = pt2
            if next1 is stop:
                pass
            else:
                pt2.next = next1
                pt1 = next1
                pt2 = next2
        if pt1 is not temp:
            temp.next = self.dummy

    def bottomUp(self, pc):
        temp = self.dummy
        for i in range(int((pc/100)*self.size)):
            temp = temp.next
        self.last.next = self.dummy.next
        self.dummy.next = temp.next
        temp.next = self.dummy
        self.last = temp

    def deRiffle(self, pc):
        if int((pc/100)*self.size) > int(self.size/2):
            a = (self.size - int((pc/100)*self.size)) - 1
            set1 = self.dummy.next
            set2 = set1.next
            temp1 = set2
            temp2 = self.dummy.next
            while temp2.next is not self.dummy:
                temp2 = temp2.next
            for i in range(a):
                set1.next = set2.next
                set1 = set1.next
                set2.next = set1.next
                set2 = set2.next
            else:
                set1.next = set2.next
                set2.next = self.dummy
                temp2.next = temp1
        else:
            a = int((pc/100)*self.size) - 1
            set1 = self.dummy.next
            set2 = set1.next
            temp = set2
            for i in range(a):
                set1.next = set2.next
                set1 = set1.next
                set2.next = set1.next
                set2 = set2.next
            else:
                set1.next = temp

    def deBottomUp(self, pc):
        temp = self.dummy
        for i in range(self.size - int(((pc)/100)*self.size)):
            temp = temp.next
        self.last.next = self.dummy.next
        self.dummy.next = temp.next
        temp.next = self.dummy
        self.last = temp

    def __str__(self):
        s = ''
        temp = self.dummy.next
        while temp is not self.dummy:
            s += str(temp)
            if temp.next is not self.dummy:
                s += ' '
            temp = temp.next
        return s


def createLL(LL):
    l = Linked_list()
    for data in LL:
        l.append(data)
    return l


def printLL(head):
    return head


def SIZE(head):
    return head.size


def scarmble(head, b, r, size):
    head.bottomUp(b)
    print(f"BottomUp {b:.3f} % :", head)
    head.riffle(r)
    print(f"Riffle {r:.3f} % :", head)
    head.deRiffle(r)
    print(f"Deriffle {r:.3f} % :", head)
    head.deBottomUp(b)
    print(f"Debottomup {b:.3f} % :", head)


inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)
