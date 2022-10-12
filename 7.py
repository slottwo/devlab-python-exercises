l = list(map(int, input().split(' ')))[:10]
print(sum(i % 2 == 0 for i in l))
