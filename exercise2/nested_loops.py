# Изведете следния pattern на конзолата:
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

for row in range(5):
    for idx in range(row):
        print('*', end=' ')
    print()

for row in range(4, 0, -1):
    for idx in range(row):
        print('*', end=' ')
    print()

# Изведете следната матрица, като умножите всеки елемент по число, въведено от потребителя.
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# Примерен вход: 4
# Изход:
# 4 8 12 16
# 20 24 28 32
# 36 40 44 48

mult_number = int(input())

for row in matrix:
    for element in row:
        print(element * mult_number, end=' ')
    print()


# Съставете матрица, като размерността ѝ се въвежда от потребителя.
# Примерен вход:
# Въведете брой редове: 2
# Въведете брой колони: 4

# Примерен изход:
# 1 2 3 4
# 5 6 7 8

rows = int(input('Въведете брой редове: '))
columns = int(input('Въведете брой колони: '))

for row in range(rows + 1):
    for col in range(1, columns + 1):
        print(col + row * columns, end=' ')
    print()
