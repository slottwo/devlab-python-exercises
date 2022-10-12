G: list = input('G: ').split(' ')

for i in range(50):
    name = input('Name: ')
    R = input('R: ').split(' ')
    
    score = sum((G[i] == R[i])/2 for i in range(20))
    
    print("Score:", score)
    print("AP" if score >= 6 else "DP")
