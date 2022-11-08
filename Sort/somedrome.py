def drome(l):
    s = 'Nondrome'
    for i in range(0,len(inp)-1):
        if l[i] == l[i+1]:
            s = 'Repdrome'
        else:
            s = 'Nondrome'
            break
    if s == 'Repdrome':
        return s
    for i in range(0,len(inp)-1):
        if l[i] <= l[i+1]:
            s = 'Mindrome'
        else:
            s = 'Nondrome'
            break
    if s == 'Mindrome':
        lset = set(l)
        if len(l) == len(lset):
            s = 'Metadrome'
        elif len(l) > len(lset):
            s = 'Plaindrome'
        return s
    for i in range(0,len(inp)-1):
        if l[i] >= l[i+1]:
            s = 'Maxdrome'
        else:
            s = 'Nondrome'
            break
    if s == 'Maxdrome':
        lset = set(l)
        if len(l) == len(lset):
            s = 'Katadrome'
        elif len(l) > len(lset):
            s = 'Nialpdrome'
        return s   
    return s  
         

inp = list(int(i) for i in input('Enter Input : '))
print(drome(inp))
