# Този файл съдържа извикването на функциите, декларирани в lib.py

from lib import sum_list, print_even_numbers
# По този начин се import-ват само определени функции от друг файл. Полезно е ако ще използваме малък брой функции
# от външна библиотека.

import lib
# По този начин се импортват всички функции от друг файл. Използва се ако ще използваме повечето функции от
# дадена библиотека с функции. Ако импортнем функция по този начин, при нейното извикване трябва да се укаже че е
# част от библиотеката.
# Примерно извикване на функция, импортирана по този начин:
# lib.is_palindrome()

sum_numbers_list = [8, 2, 3, 0, 7]

# При извикването на функция тя връща стойност. Присвояваме тази стойност към променлива.
sum_of_numbers = sum_list(sum_numbers_list)
print(sum_of_numbers)

##################

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Тази функция няма указан return. Тя винаги връща None като стойност. Приложението ѝ е само за да извежда данни.
print_even_numbers(sample_list)

##################

check_palindrome = input('Въведете текст за проверка за палиндром:')

# Можем да използваме извикването на функциите по такъв начин, какъвто ни е нужен.
# За конкретната задача не ни е нужно стойността, която функцията връща да се записва в променлива.
print(lib.is_palindrome(check_palindrome))

##################

password = input('Въведете парола: ')
is_valid_password = lib.password_validator(password)

# правим бърза проверка, за да може да изведем текст вместо само True/False
is_valid_text = 'Valid' if is_valid_password else 'Not valid'

print(is_valid_text)

##################

# Python позволява изписването на подобен трудно четим код
# В този ред едновременно се въвежда числото, което се подава във функцията
# Функцията се изпълнява и връща стойност, която ние извеждаме в конзолата
print(lib.fact(int(input("Въведете число за изчисление на факториел:"))))

# --------------------------------
# ЗАДАЧА ЗА ВКЪЩИ (по желание)
# Прегледайте дадените решения на задачите и измислете алтернативен вариант за решение