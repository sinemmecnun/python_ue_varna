# Полезни линкове
# https://www.w3schools.com/python/python_datatypes.asp
# https://www.geeksforgeeks.org/python-data-types/

# Python не е строго типизиран език като други езици от високо ниво
string_variable = 'text'

int_variable = 674354

float_variable = 453.4556

list_variable = [1, 45, 3.244, 'some text']
# set и tuple също са видове списъци
# разликата между list, tuple и set: list е подреден списък, чиято дължина и елементи могат да бъдат променени,
# при tuple същите не могат да бъдат променени след като е дефиниран tuple-a
# set е списък с особеността, че съдържа единствено уникални елементи - не може да има дублиращи се елементи

# dictionary е неподреден списък, като всеки елемент се състои от ключ и стойност. За разлика от списъците,
# елементите в dictionary-тата не могат да се достъпват по индекс (нямат такъв), а се достъпват по ключ
dictionary_variable = {
    1: 'strawberries',
    2: 'raspberry',
    'key': 'value'
}

# достъпване на стойност на ключ в речник
print(dictionary_variable['key'])

boolean_variable = False

# с type(var) може да се провери типът на дадена променлива
print(type(string_variable))

# кастване към int и float на вход

int_var = int(input())

float_var = float(input())


name = 'Ivan'
city = 'Varna'
age = 17.7854

# Извеждане на текст, използвайки конкатенация. Няма възможност за директна работа с числови променливи,
# необходимо е да се кастнат към текст
print('i am ' + name + '. I live in ' + city + '.' + "I am " + str(age) + ' years old')

# Извеждане на текст използвайки интерполация. Може директно да се изведат числови променливи
print(f"I am {name}. I live in {city}. I am {age:.2f} years old")
# :.2f се използва за форматиране на число до определен брой след десетичната запетая (в случая 2)


# print() добавя празен ред след изведения текст, освен ако не се зададе друго, използвайки end=''
# end='' задава че няма да има никакво празно пространство след изведения текст
# могат да се използват всякакви стрингове като край на изведения стринг с print
print('i am ivan', end='')
print("i live in")

print('i am ivan', end='...')
print("i live in")