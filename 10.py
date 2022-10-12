G: list = input('G: ').split(' ')
students: list[dict] = []
for i in range(50):
    student = {}
    student['name'] = input('Name: ')
    R = input('R: ').split(' ')
    student['score'] = sum((G[i] == R[i])/2 for i in range(20))
    students.append(student)

for student in students:
    print(student['name'],
          "AP" if student['score'] >= 6 else "DP",
          sep='\n')
