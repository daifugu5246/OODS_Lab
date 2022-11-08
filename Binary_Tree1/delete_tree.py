class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        temp = self.root
        if self.root is None:
            self.root = Node(val)
        else:
            temp = self.root
            while val < temp.data:
                if temp.left is None:
                    temp.left = Node(val)
                    break
                else:
                    temp = temp.left
            while val >= temp.data:
                if temp.right is None:
                    temp.right = Node(val)
                    break
                else:
                    temp = temp.right
                    while val < temp.data :
                        if temp.left is None:
                            temp.left = Node(val)
                            break
                        else:
                            temp = temp.left       
        return self.root

    def delete(self,data):
        self.root = BinarySearchTree._delete(self.root,data)
      
    def _delete(r, data):
        if r is None:
            print("Error! Not Found DATA")
            return
        if r.left is None and r.right is None and r.data == data:
            r = None
            return r
        elif r.left is None and r.data == data:
            r = r.right
            return r
        elif r.right is None and r.data == data:
            r = r.left
            return r
        elif r.data == data:
            cur = r.right 
            while cur.left != None: 
                cur = cur.left 
            r.data = cur.data
            r.right = BinarySearchTree._delete(r.right,cur.data)
        else:
            if r.data > data:
                r.left = BinarySearchTree._delete(r.left,data)
            else:
                r.right = BinarySearchTree._delete(r.right,data)
        return r

    def MIN(self):
        min = self.root
        while min.left is not None and min.left.data < min.data:
            min = min.left
        return min

    def inOder(self):
        BinarySearchTree._inOder(self.root)

    def _inOder(root,data):
        if root is not None:
            BinarySearchTree._inOder(root.left)
            print(root,end = ' ')
            BinarySearchTree._inOder(root.right)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    commamd,val = i.split()
    val = int(val)
    if commamd == 'i':
        print(f"insert {val}")
        root = tree.insert(val)
        printTree90(tree.root)
    else:
        print(f"delete {val}")
        tree.delete(val)
        printTree90(tree.root)
