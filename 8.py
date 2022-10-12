odd = []
even = []
try:
    while True:
        x = int(input())
        if x % 2:
            if len(even) < 4:
                even.append(x)
            else:
                print('Even:', *even, x)
                even = []
        else:
            if len(odd) < 4:
                odd.append(x)
            else:
                print('Odd:', *odd, x)
                odd = []
except:
    if even:
        print('Remaining even:', *even)
    if odd:
        print('Remaining odd:', *odd)
