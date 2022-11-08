class Node:
    def __init__(self,key = None,value = 0,right = None,left = None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self) -> str:
        return f'N({self.key},{self.value})'

    def printTree(node, level = 0):
        if node != None:
            Node.printTree(node.right, level + 1)
            print('     ' * level, node)
            Node.printTree(node.left, level + 1)
    
inp = input('Enter Input : ').split('/')
K = [i for i in range(1,int(inp[0])+1)]
book = [int(i) for i in inp[1].split()]
tree_list = [Node(i) for i in K]
for i in tree_list[::]:
    i.left = None if 2*tree_list.index(i) + 1 > len(tree_list) - 1 else tree_list[2*tree_list.index(i) + 1]
    i.right = None if 2*tree_list.index(i) + 2 > len(tree_list) - 1  else tree_list[2*tree_list.index(i) + 2]
cus_count = 1
while len(book) > 0:
    for i in tree_list:
        if i.value > 0:
            i.value -= 1
    for i in tree_list:
        if i.value == 0 and len(book) > 0:
            i.value = book.pop(0)
            print(f'Customer {cus_count} Booking Van {i.key} | {i.value} day(s)')
            cus_count += 1