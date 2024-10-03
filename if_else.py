# check whether a number if even or odd
check_number = int(input())

# първи начин
if check_number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

# втори начин
is_even = True if check_number % 2 == 0 else False
print(is_even)


# check if a number is divisible by 3
number = int(input())

is_divisible = False
if number % 3 == 0:
    is_divisible = True

print(is_divisible)

# input a number and check if it is divisible by 3 and 2. if it is not check if the number is divisible by 4 or 5

number = int(input())

if number % 3 == 0 and number % 2 == 0:
    print(f'{number} is divisible by 3 and 2')
elif number % 4 == 0 or number % 5 == 0:
    print(f'{number} is divisible by 4 or 5')
else:
    print(f'{number} is not divisible by either number')


# print days of the week assuming that the first day of the week is Monday
# example input - output:
# 1 - Monday

day_of_the_week = int(input())

if day_of_the_week == 1:
    print('Monday')
elif day_of_the_week == 2:
    print('Tuesday')
elif day_of_the_week == 3:
    print('Wednesday')
elif day_of_the_week == 4:
    print('Thursday')
elif day_of_the_week == 5:
    print('Friday')
elif day_of_the_week == 6:
    print('Saturday')
elif day_of_the_week == 7:
    print('Sunday')
else:
    print('Incorrect input')

# Да се въведе стойността на поръчка и да се изчисли крайната цена като се приспадне отстъпката.
# Отстъпките са над 100 лв включително - 11% отстъпка и над 999 лв - 23% отстъпка.
# Да се изведе крайната цена форматирана до 2 цифри след десетичната запетая

price = float(input())

if price <= 0:
    print('Incorrect input')
elif price >= 100:
    price *= 0.89
elif price > 999:
    price *= 0.77

print(f'Final price: {price:.2f} lv')

# find the greater of two numbers and print it. if the numbers are equal print 'The numbers are equal'
number_one = int(input())
number_two = int(input())

if number_one > number_two:
    print(f'{number_one} is greater than {number_two}')
elif number_one < number_two:
    print(f'{number_two} is greater than {number_one}')
else:
    print('The numbers are equal')