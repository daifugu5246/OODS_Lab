def length(txt):
    if txt == '':
        return 0

    print(txt[0]+'*',end='')

    if txt[1:] == '':
        return 1

    print(txt[1]+'~',end='')

    return length(txt[2:]) + 2

print("\n", length(input("Enter Input : ")), sep="")
