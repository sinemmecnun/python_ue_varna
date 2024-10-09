# Write a Python function that returns sum all the numbers in a list.
# Sample List : [8, 2, 3, 0, 7]
# Expected Output : 20

def sum_list(list_temp):
    return sum(list_temp)


# Write a Python function to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : 2 4 6 8

def print_even_numbers(list_temp):
    for element in list_temp:
        if element % 2 == 0:
            print(element, end=' ')
    print()


def print_even_numbers_2(list_temp):
    final_list = []
    for element in list_temp:
        if element % 2 == 0:
            final_list.append(element)
    print(final_list)


# Напишете функция, която проверява дали дадено число/стринг е палиндром и връща True/False
# Примерен вход: 12233221
# Примерен изход: True
#
# Примерен вход: is palindrome?
# Примерен изход: False


def is_palindrome(check_string):
    return check_string == check_string[::-1]
# използван е slicing, който се използва при стрингове и списъци. Конкретния случай той се използва за
# reverse-ване на стринга


# Напишете функция, която да проверява дали дадена парола отговаря на изискванията. Изискванията са:
# Да е с дължина поне 8 символа
# Трябва да съдържа само букви и цифри

def password_validator(password_string):
    is_valid = True
    if len(password_string) < 8:
        is_valid = False
        return is_valid
    if not password_string.isalnum():
        is_valid = False
    return is_valid


# Напишете функция, която да намира факториела на число въведено от потребителя.

# Най-често за намиране на факториел се използва рекурсивна функция
# Рекурсията е функция, която извиква себе си. Изпълнението на тези функции наподобява цикъл.
# За да може да се спре изпълнението на рекурсивна функция, така че да не попадне в безкраен цикъл, всяка такава функция
# има нужда от дъно - условие което да прекъсне повторното извикване на функцията


def fact(number):
    if number > 0:
        return number * fact(number - 1)
    return 1


# Тази задача може да се реши и използвайки цикъл - как?

