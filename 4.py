patients: list[dict] = []
while True:
    patients.append({
        'value': float(input("Indemnity: R$ ").replace(',', '.')),
        'age': int(input("Age: [yeas] ")),
        'name': input("Full Name: ")
    })
    if input("Continue? [Y/n] ") not in "Yy":
        break


def increase(age: int) -> float:
    if age < 13:
        return 1.3
    if age < 50:
        return 1.1
    if age < 60:
        return 1.15
    return 1.35


for i, patient in enumerate(patients):
    patient['name'] = ' '.join(
        map(lambda s: s.capitalize(), patient['name'].split(' ')))
    patient['value'] *= increase(patient['age'])
    print(
        f"Patient {i+1}: {patient['name']}, {patient['age']} years old. Indemnity: R$ {patient['value']:.2f}")
