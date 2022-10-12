n = int(input())
V: list[tuple[float]] = []
N: list[float] = []
for i in range(3):
    V.append(tuple(map(float, input().replace(',', '.').split(' ')))[:n])
    # a
    N.append(sum(x**2 for x in V[i])**0.5)
print("Highest norm:", round(max(N), 1))
print("Vector Sum:", *tuple(map(lambda *t: sum(t), *V)))
