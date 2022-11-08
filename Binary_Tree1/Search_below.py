class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            temp = self.root
            while data < temp.data:
                if temp.left is None:
                    temp.left = Node(data)
                    break
                else:
                    temp = temp.left
            while data >= temp.data:
                if temp.right is None:
                    temp.right = Node(data)
                    break
                else:
                    temp = temp.right
                    while data < temp.data:
                        if temp.left is None:
                            temp.left = Node(data)
                            break
                        else:
                            temp = temp.left   

    def MIN(self):
        min = self.root
        while min.left is not None and min.left.data < min.data:
            min = min.left
        return min.data

    def below(self,num):
        BST._below(self.root,num)

    def _below(root,num):
        if root is not None:
            BST._below(root.left,num)
            if root.data < num:
                print(root,end = ' ')
            BST._below(root.right,num)

    def printTree(self):
        BST._printTree(self.root)

    def _printTree(node, level = 0):
        if node != None:
            BST._printTree(node.right, level + 1)
            print('     ' * level, node)
            BST._printTree(node.left, level + 1)
T = BST()
ns , n = input('Enter Input : ').split('|')
n = int(n)
nums = [int(i) for i in ns.split()]
for i in nums:
    T.insert(i)
T.printTree()
print("--------------------------------------------------")
print(f"Below {n} : ",end = '')
if n <= T.MIN():
    print("Not have")
else:
    T.below(n)