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
                    
        return self.root

    def checkpos(self,data):
        if data == self.root.data:
            print("Root")
            return 
        else:
            if BST._checkpos(self.root,data) is True:
                return
            else:
                print("Not exist")
                return


    def _checkpos(root,data, f = False):
        if root is not None:
            BST._checkpos(root.left,data,f)
            if root.data == data and root.left is None and root.right is None:
                f = True
                print("Leaf")
                exit(0) 
            elif root.data == data and (root.left is not None or root.right is not None):
                f = True
                print("Inner")
                exit(0)
            BST._checkpos(root.right,data,f)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])