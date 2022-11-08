class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.key)
    
"""
Binary tree
มีมากที่สุดได้เพียง 2 subtree
์Node ด้านซ้ายจะ < กว่าเเละ Node ทางด้านขวาจะ >= Node root ของตัวมันเองเสมอ
"""
class BST:
    def __init__(self):
            self.root = None

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            root = self.root
            while key < root.key:
                if root.left is None:
                    root.left = Node(key)
                    return self.root
                else:
                    root = root.left
            while key >= root.key:
                if root.right is None:
                    root.right = Node(key)
                    return self.root
                else:
                    root = root.right
                    while key < root.key:
                        if root.left is None:
                            root.left = Node(key)
                            return self.root
                        else:
                            root = root.left
        return self.root

    def printTree(self,node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
#Traversal : Breadth first ไปด้านข้างก่อน:ไปหาลูกทุกคนเเล้วค่อยไปหลาน
def levelOrder(root):
    if root is None:
        return 
    q = []
    q.append(root)
    while len(q) > 0:
        print(q[0],end = ' ')
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
#Traversal : Depth  first ไปด้านลึกก่อน:ไปหาลูกคนเเรกเเล้วค่อยไปหลานของรูกคนเเรกเเล้วย้ายไปลูกคนถัดไป
def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    #update or print data
    print(root,end=' ')
    inOrder(root.right)

def preOrder(root):
    if root is None:
        return
    #update or print data
    print(root,end=' ')
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    #update or print data
    print(root,end=' ')
    
tree = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = tree.insert(i)
tree.printTree(root)
print('Level Order : ',end='')
levelOrder(root)
print()
print('InOrder : ',end='')
inOrder(root)
print()
print('PreOrder : ',end='')
preOrder(root)
print()
print('PostOrder : ',end='')
postOrder(root)
