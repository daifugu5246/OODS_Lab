class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
    def setData(self,data):
        self.data = data

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

    def mul_over(self,value):
        BST._mul_over(self.root,value)
    
    def _mul_over(root,value):
        if root is not None:
            BST._mul_over(root.left,value)
            if root.data > value:
                root.setData(root.data*3)
            BST._mul_over(root.right,value)

    def inOder(self):
        BST._inOder(self.root)

    def _inOder(root):
        if root is not None:
            BST._inOder(root.left)
            print(root,end = ' ')
            BST._inOder(root.right)

    def printTree(self):
        BST._printTree(self.root)

    def _printTree(node, level = 0):
        if node != None:
            BST._printTree(node.right, level + 1)
            print('     ' * level, node)
            BST._printTree(node.left, level + 1)
T = BST()
ns , n = input('Enter Input : ').split('/')
n = int(n)
nums = [int(i) for i in ns.split()]
for i in nums:
    T.insert(i)
T.printTree()
print("--------------------------------------------------")
T.mul_over(n)
T.printTree()

