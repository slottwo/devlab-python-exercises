clients: list[dict] = []
while True:
    clients.append({
        'name': input("Name: "),
        'rg': tuple(map(int, input("RG: ").split('-')))[:2],
        'cpf': int(input("CPF: ").remove('.').remove('-')[:11]),
        'ddd': int(input("DDD: ")[:2]),
        'phone': int(input("Phone number: ").remove('-'))
    })
    if input("Continue? [Y/n] ") not in "Yy":
        break

print()
for i, client in enumerate(clients):
    client['name'] = ' '.join(
        map(lambda s: s.strip().capitalize(), client['name'].split(' ')))

    cpf = str(client['cpf'])
    phone = str(client['phone'])

    print(f"Client {i+1}: ",
          f"Name {client['name']}",
          f"RG: {client['rg'][0]}-{client['rg'][1][0]}",
          f"CPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[-2:]}",
          f"Phone: ({client['ddd']}) {phone[:len(phone-4)]}-{phone[4:]}")
