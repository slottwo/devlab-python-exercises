a = int(input('a: '))
b = int(input('b: '))

if a > b:
    a, b = b, a

N = int(input('N: '))
print('Vector V: ')
V = (int(input()) for i in range(N))
print(*set(filter(lambda x: x <= b, filter(lambda x: x >= a, V))))
