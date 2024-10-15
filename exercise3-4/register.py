# Прочетете от конзолата данни за нов клиент - име и фамилия, години, ЕГН, IBAN, телефонен номер.
# Валидирайте въведените данни и ги запишете в списък:
# - името и фамилията да се прочетат по отделно, но да се конкатенират при запис в списъка. Да се провери, че не съдържат цифри
# - годините не могат да са отрицателно число и трябва да е число по-голямо от 0. За да може да бъде регистриран клиент,
# трябва да е на поне 18 години.
# - ЕГН - 10 цифри
# - IBAN - първите 2 символа да са букви, дължината може да е до 34 символа
# - телефонен номер - 10 цифри, трябва да е български номер - да започва с 089, 087, 088 или 098
# Изведете всички данни на клиента в следния формат, готов за експорт към csv:
# Име Фамилия,години,ЕГН,IBAN,телефонен номер
# Прочетете от конзолата данни за нов клиент - име и фамилия, години, ЕГН, IBAN, телефонен номер.

all_clients_data = []

# - името и фамилията да се прочетат по отделно, но да се конкатенират при запис в списъка. Да се провери, че не съдържат цифри
while True:
    client_data = []
    while True:
        name = input('Въведете име: ')
        is_name_valid = True
        for s in name:
            if s.isdigit():
                is_name_valid = False
                break

        if is_name_valid:
            break

    while True:
        lastname = input('Въведете фамилия: ')
        is_lastname_valid = True
        for s in lastname:
            if s.isdigit():
                is_lastname_valid = False
                break
        if is_lastname_valid:
            break

    client_data.append(f'{name} {lastname}')

    # - годините не могат да са отрицателно число и трябва да е число по-голямо от 0. За да може да бъде регистриран клиент,
    # трябва да е на поне 18 години.

    while True:
        age = input('Въведете години: ')

        if age.isdigit() and int(age) >= 18:
            client_data.append(age)
            break

    # - ЕГН - 10 цифри

    while True:
        egn = input('Въведете ЕГН: ')
        if egn.isdigit() and len(egn) == 10:
            client_data.append(egn)
            break

    # - IBAN - първите 2 символа да са букви, дължината може да е до 34 символа
    while True:
        iban = input('Въведете IBAN: ')

        is_iban_valid = True
        if len(iban) > 34:
            is_iban_valid = False

        if not iban[0:2].isalpha():
            is_iban_valid = False

        if is_iban_valid:
            client_data.append(iban)
            break

    # - телефонен номер - 10 цифри, трябва да е български номер - да започва с 089, 087, 088 или 098
    while True:
        phone_number = input('Въведете телефонен номер: ')

        is_number_valid = True
        if not len(phone_number) == 10 or not phone_number.isdigit():
            is_number_valid = False
        else:
            phone_operators = ['089', '088', '087', '098']
            if not phone_number[0:3] in phone_operators:
                is_number_valid = False

        if is_number_valid:
            client_data.append(phone_number)
            break

    # Изведете всички данни на клиента в следния формат, готов за експорт към csv:
    # Име Фамилия,години,ЕГН,IBAN,телефонен номер

    all_clients_data.append(client_data)

    print('Натиснете 1 за изход, 2 за да добавите нов клиент')
    action = input()
    if action == '1':
        break


for client in all_clients_data:
    print(','.join(client))