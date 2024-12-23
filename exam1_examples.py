# 1.	Да се въведе сума без ДДС и да се пресметне колко е сумата на ДДС и колко е сумата с включен ДДС (20%).
# Изходът да се форматира по начина, показан в примера.
# Примерен вход:
# Въведете сума без ДДС: 220
# Изход:
# Сума на ДДС: 44.00 лв. Сума с ДДС: 264.00 лв.

sum_without_dds = float(input('Въведете сума без ДДС: '))

dds_amount = sum_without_dds * 0.2
sum_with_dds = sum_without_dds + dds_amount

print(f'Сума на ДДС: {dds_amount:.2f} лв. Сума с ДДС: {sum_with_dds:.2f} лв.')

# 2.	Клиент купува кола и трябва да му се приложи отстъпка. Отстъпката се изчислява според годината на автомобила и
# се прилагат следните правила:
# a.	2010 – 2024 – 5 % отстъпка
# b.	2000 – 2009 – 15 % отстъпка
# c.	1980 – 1999 – 25 % отстъпка
# d.	Всички останали години – няма отстъпка
# На всеки автомобил се добавя 1000 лв застраховка в крайната цена. Застраховката не участва в сумата за определяне на
# отсъпката, тя се добавя накрая.
# При въведени сума и година на автомобила, върнете общата сума, която клиентът трябва да заплати.

year = int(input('Въведете година: '))
initial_sum = float(input('Въведете сума: '))
final_sum = initial_sum

#
if 1980 <= year <= 1999:
    final_sum *= 0.75
elif 2000 <= year <= 2009:
    final_sum *= 0.85
elif 2020 <= year <= 2024:
    final_sum *= 0.95

final_sum += 1000
print(f'Крайна сума: {final_sum:.2f} лв')

# 3.	Забийте в кода дадено число. Задачата на потребителя е да познае това число. Дайте му по ваше желание или
# безброй опити или определен брой опити да познае числото. Ако въведеното от потребителя число при даден опит наближава
# отговора му върнете „Топло“, иначе върнете „Студено“. За условие за набижаване да се приеме, ако въведеното число е в
# интервала [отговор – 5;отговор+5].
#
# Пример:
# Задаваме като отговор 43
#  Интервалът за приближаване е [38;48] – Топло
# Всичко останало е студено.
# Задаваме броя опити на 10.

answer = 43
number_of_tries = 10

for x in range(0, 10):
    number = int(input())
    if number == answer:
        print('Познахте!')
        break
    if answer - 5 <= number <= answer + 5:
        print('Топло')
        continue
    print('Студено')


# 4.	Напишете функция, която приема като аргументи код на статус и връща с текстов формат статуса.
# Използвайте функцията и върнете статуса в текстов формат. Мапинг на статусите (код-текст).
# Всички останали кодове са невалидни (върнете текст „Not found“).
# 1 – Canceled
# 2 – Pending
# 3 – Confirmed
# 4 – Expired

#  Вариант 1
def get_status(code):
    if code == 1:
        return 'Canceled'
    if code == 2:
        return 'Pending'
    if code == 3:
        return 'Confirmed'
    if code == 4:
        return 'Expired'
    return 'NotFound'


# Вариант 2
def get_status2(code):
    status = 'NotFound'

    if code == 1:
        status = 'Canceled'
    elif code == 2:
        status = 'Pending'
    elif code == 3:
        status = 'Confirmed'
    elif code == 4:
        status = 'Expired'

    return status


status_code = int(input())
status_text = get_status(status_code)
print(status_text)

# 5.    Напишете функция, която получава като аргументи текст и платежна система като число.
# Да се определи дали този текст отговаря на изискванията за дължина на платежната система и ако не отговаря,
# да се отреже така че да отговаря.
# Платежна система 1 – ограничение 70 символа
# Платежна система 2 и 3 – ограничение 35 символа
# Други платежни системи – няма изискване/не се знае – няма да се правят промени


def trim_text(text, system):
    if system == 1:
        if len(text) > 70:
            return text[:70]
    if system == 2 or system == 3:
        if len(text) > 35:
            return text[:35]
    return text


text = input()
payment_system = int(input('Въведете платежна система: '))

trimmed_text = trim_text(text, payment_system)
print(trimmed_text)
