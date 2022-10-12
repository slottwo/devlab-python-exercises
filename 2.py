l = list(map(int, input("Enter 10 integers separated by spaces: ").split(' ')))
print(*l[:10])
x = int(input("Enter a integer you want to search: "))
print(f"The number {x} {'' if x in l else 'not '}is in the list.")
