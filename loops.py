# Циклите се използват, за да предотвратят писането на повтарящ се код.
# Те правят мащабирането на повтарящи се операции по-лесни - един цикъл може да се приложи по еднакъв начин върху
# списък от 10 елемента или от 10000 елемента. В python има 3 вида цикли:

while True:
    break

# while цикълът се изпълнява докато зададеното условие не стане False.
# while True циклите са безкрайни. Проверката, която ще прекъсне цикъла се задава в тялото на цикъла като се използва break.

for var in range(start_number, end_number, step):
    break

# for ... in range() циклите се изпълняват определен брой пъти зададени от цикъла.
# Трябва да се зададе начало и край на цикъла.
# Този тип цикъл също е полезен ако работим с индексите на елементите даден списък

for element in list:
    break

# for ... in ... циклите се използват главно при работа със списъци. С този тип цикъл може директно да
# достъпим стойностите на елементите в списък.

# break се използва за прекъсване на цикъл
# continue се използва за прекъсване на текущото изпълнение на цикъла и преминаване към следващото "въртене"

# Задачи
# Изведете всички числа от 1 до 10 - for loop, while loop

# първи начин
for number in range(1, 11, 1):
    print(number)

# втори начин
for number in range(1, 11):
    print(number)

# трети начин
number = 1
while number <= 10:
    print(number)
    number += 1

# четвърти начин
start_number = 1
while True:
    if start_number >= 10:
        break
    print(start_number)
    start_number += 1


# Изведете всички числа от 1 до 10 през 2

# първи начин
for number in range(1, 11, 2):
    print(number)

# втори начин
number = 1
while number <= 10:
    print(number)
    number += 2

# Изведете всички числа от 10 до 1

# първи начин
for number in range(10, 0, 1):
    print(number)

# втори начин
for number in range(10, 0):
    print(number)

# трети начин
number = 10
while number > 0:
    print(number)
    number -= 1

# Изведете всички числа от 10 до 1 през 2

# първи начин
for number in range(10, 0, 2):
    print(number)

# втори начин
number = 10
while number > 0:
    print(number)
    number -= 2


# Въведете число и изведете всички четни числа от 1 до въведеното число

# първи начин
user_number = int(input())
for num in range(2, user_number + 1, 2):
    print(num)

# втори начин
# list comprehension - ще бъде разгледано на упражнението за списъци
[print(num) for num in range(2, user_number + 1, 2)]

# Изведете всички четни числа в даден списък
example_list = [1, 6, 3, 53, 63, 12, 45, 23]

# първи начин
for num in example_list:
    if num % 2 == 0:
        print(num)

# втори начин
for index in range(len(example_list)):
    num = example_list[index]
    if num % 2 == 0:
        print(num)

# трети начин
[print(num) for num in example_list if num % 2 == 0]

# Изведете елементите намиращи се на нечетни индекси в дадения списък
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for index in range(1, len(my_list), 2):
    print(my_list[index])
