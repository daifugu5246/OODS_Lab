class Node: 
    def __init__(self,key,value = 0):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

    def __repr__(self) -> str:
        return f"N({self.key}, {self.value})"

    def printTree(node, level = 0):
        if node != None:
            Node.printTree(node.right, level + 1)
            print('     ' * level, node)
            Node.printTree(node.left, level + 1)

def encode(root,code = '',code_dict={}):
    if root.left is None and root.right is None:
        code_dict[root.key] = code
        return code_dict
    code += '1'
    code_dict = encode(root.right,code,code_dict)
    code = code[:-1]
    if root.left is not None:
        code += '0'
        code_dict = encode(root.left,code,code_dict)
    return code_dict
    

def getKey(x):
    if x.key == '*':
        return 0
    else:
        return ord(x.key)
        
def getValue(x):
    return x.value

inp = list(input("Enter Input : ")) 
amount = {i:inp.count(i) for i in inp}
node_list = [Node(i,amount[i]) for i in amount]
while len(node_list) > 1: 
    node_list.sort(key=getKey)
    node_list.sort(key=getValue)
    a = node_list.pop(0)
    b = node_list.pop(0)
    a, b = sorted(sorted([a, b], key=getKey), key=getValue)
    root = Node('*',a.value + b.value)
    root.left = a
    root.right = b
    node_list.append(root)
code_dict = encode(node_list[0])
print(code_dict)
node_list[0].printTree()
encoded = ''.join([code_dict[i] for i in inp])
print(f'Encoded! : {encoded}')

