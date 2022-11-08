#Color_Crush
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return True if self.size() == 0 else False


inp = input('Enter Input : ').split()
S = Stack()
Combo, count = 0, 1
for i in inp:
    S.push(i)
#S [B A A A C]
while True:
    LS = S.size()  # Last size of Stack  2
    t = Stack()  # tempStack []
    c = ""  # characterCheck ""
    while not S.isEmpty():
        x = S.pop() #S[B C] | x = "B"
        if c != x: #c="A"
            c = x #c="B"
            count = 1
        else:
            count += 1 #count = 3
        t.push(x) #t [C B]
        if count == 3:  # Explode
            Combo += 1 #Combo = 1
            for i in range(3):
                t.pop() #t [C B]

    while not t.isEmpty(): 
        S.push(t.pop()) #S[B C] | #t []

    #S[B C]
    # 2      #2
    if LS == S.size():
        break

print(S.size())
if S.isEmpty():
    print("Empty", end="")
else:
    for i in range(S.size()):
        print(S.pop(), end="")
if Combo > 1:
    print(f"\nCombo : {Combo} ! ! !")