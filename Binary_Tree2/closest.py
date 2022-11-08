class Node:
    def __init__(self,data):
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

    def closer(root,curr,n):
            if abs(root - n) < abs(curr - n):
                return root
            elif abs(root - n) == abs(curr - n):
                if root > curr:
                    return root
                else:
                    return curr
            else:
                return curr

    def closest(self,root,n,curr = None):
        if root.left is None and root.right is None:
            if curr is None:
                return root.data
            else:
                return BST.closer(root.data,curr,n)

        if root.left is None and root.right is not None:
            curr = self.closest(root.right,n,curr)
            return BST.closer(root.data,curr,n)
        curr = self.closest(root.left,n,curr)
        if root.right is None :
            return BST.closer(root.data,curr,n)
        curr = self.closest(root.right,n,curr)
        return BST.closer(root.data,curr,n)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

inp,n =  input('Enter Input : ').split('/')
n = int(n)
tree = BST()
root = None
l = inp.split()
for i in l:
    root = tree.insert(int(i))
    tree.printTree(root)
    print("--------------------------------------------------")
print(f"Closest value of {n} : {tree.closest(root,n)}")