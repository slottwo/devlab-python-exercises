l = list(map(float, input(
    "Enter 10 real numbers separated by spaces: ").replace(',', '.').split(' ')))
l = l[:10]

neg = 0
for i in l:
    neg += i < 0

# n = ''.join(l).count('-')

print("Average:", round(sum(l)/10, 2))
print("Highest:", max(l))
print("Lowest:", min(l))
print("Negatives:", neg)
print("Positives:", 10 - neg - l.count(0))
