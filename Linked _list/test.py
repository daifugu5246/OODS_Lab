def factorial(n):
    if n-1 > 0:
        return n*(factorial(n-1))
    else:
        return 1

def sum(n,l):
    if n < len(l) and n >= 0:
        return l[n] + sum(n-1,l)
    elif n >= len(l):
        n = len(l)-1
        return l[n] + sum(n-1,l)
    else: 
        return 0

def fibR(n):
    if n <= 1:
        return n
    else:
        return fibR(n-1) + fibR(n-2)
 
print(fibR(10))