def combinations(l):
    if len(l) == 0:
        return [[]]
    combos = []
    for combo in combinations(l[1:]):
        combos += [combo , combo + [l[0]]]
    return combos 
        
def mini(l):
    if len(l) == 0:
        return
    elif len(l) == 1:
        temp = l[0].split()
        S = int(temp[0])
        B = int(temp[1])
        return abs(S - B)
    elif len(l) > 1:
        S = 1
        B = 0
        for i in l:
            temp = i.split()
            S *= int(temp[0])
            B += int(temp[1])
        return abs(S-B)

inp = input("Enter Input : ").split(',')
comb = combinations(inp)
comb.remove([])
result = list(map(mini,comb))
print(result)