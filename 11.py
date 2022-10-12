l = list(map(int, input("Enter 15 numbers: ").split(' ')))[:15]
print('[0: stop, 1: show, 2: reverse show]')
code = int(input("Code: "))
if code == 1:
    print(*l)
elif code == 2:
    print(*l[::-1])
