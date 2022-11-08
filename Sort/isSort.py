inp = [int(i) for i in input("Enter Input : ").split()]
isSort = True
for i in range(len(inp)-1):
    if inp[i] > inp[i+1]:
        isSort = False
        break
print('Yes' if isSort else 'No')