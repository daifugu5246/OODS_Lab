def staircase(n, w=None):
    if n == 0:
        return 'Not Draw!'
    if w is None:
        w = n-1 if n > 0 else 0
    stop = -1 if n > 0 else -n
    if w == stop:
        return ''
    return '_'*w + '#'*(abs(n)-w) + '\n' + staircase(n, w-1 if n > 0 else w+1)


print(staircase(int(input("Enter Input : "))), end='')
