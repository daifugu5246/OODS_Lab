class Node:
    def __init__(self,data = None,right = None,left = None):
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self) -> str:
        return f'N({self.data})'

    def printTree(node, level = 0):
        if node != None:
            Node.printTree(node.right, level + 1)
            print('     ' * level, node)
            Node.printTree(node.left, level + 1)

    def sumTree(root):
        if root.left is None and root.right is None:
            return root.data
        sum = root.data + Node.sumTree(root.left)
        if root.right is not None:
            sum += Node.sumTree(root.right)
        return sum

def oparetor(a,b):
    return '>' if a > b else '<' if a < b else '=' 
    

inp = input('Enter Input : ').split('/')
power = list(int(i) for i in inp[0].split())
comp = list(list(int(j) for j in i.split()) for i in inp[1].split(','))
tree_list = [Node(i) for i in power]
for i in tree_list[::]:
    i.left = None if 2*tree_list.index(i) + 1 > len(tree_list) - 1 else tree_list[2*tree_list.index(i) + 1]
    i.right = None if 2*tree_list.index(i) + 2 > len(tree_list) - 1  else tree_list[2*tree_list.index(i) + 2]

print(tree_list[0].sumTree())

for i in comp:
    a = tree_list[i[0]].sumTree()
    b = tree_list[i[1]].sumTree()
    print(f'{i[0]}{oparetor(a,b)}{i[1]}')