def toInteger(s):
    value = 0
    for i in list(s):
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            continue
        else:
            value = i
    return value

def selection(l):
    for last in range(len(l)-1,0,-1):
        biggest = toInteger(l[0])
        biggest_i = 0
        for i in range(1,last+1):
            if toInteger(l[i]) > biggest:
                biggest = toInteger(l[i])
                biggest_i = i
        
        l[last],l[biggest_i] = l[biggest_i],l[last]

inp = input('Enter Input : ').split()
selection(inp)
print(*inp,sep = ' ')