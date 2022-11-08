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

    def insert(self,data):
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

    def rank(self,root,n,curr=None,r=0):
        if root.left is None and root.right is None:
            if n < root.data:
                print(r)
                exit(0)
            else:
                return root.data,r+1

        if root.left is None and root.right is not None:
            if curr is None and root is self.root:
                if n < root.data:
                    print(r)
                    exit(0)
                else:
                    r = r + 1
                    curr = root.data
                    curr,r = self.rank(root.right,n,curr,r) 
            if n < root.data and n >= curr:
                print(r)
                exit(0)
            elif root is self.root and n >= curr:
                print(r)
                exit(0)
            else:
                r = r + 1
                curr = root.data
                curr,r = self.rank(root.right,n,curr,r)
                return curr,r
        curr,r = self.rank(root.left,n,curr,r)
        if n < root.data and n >= curr:
            print(r)
            exit(0)
        if root.right is None :
            return root.data,r+1
        else:
            r = r + 1
            curr = root.data
            curr,r = self.rank(root.right,n,curr,r)
        if n < root.data and n >= curr:
            print(r)
            exit(0)
        else:
            return curr,r

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
                
l,n = input('Enter Input : ').split('/')
n = int(n)
l = list(map(int,l.split()))
tree = BST()
for i in l:
    root = tree.insert(i)
tree.printTree(root)
print('--------------------------------------------------')
print(f'Rank of {n} : ',end="")
tree.rank(root,n)
