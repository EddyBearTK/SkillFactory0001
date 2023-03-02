print("Приветствую в игре Крестики-нолики (X-O)!")
#input('Введи адрес ячейки, где хочешь поставить Х в формате: 1 цифра - ряд, 2 цифра - колонка')
fields = [['-']*3 for _ in range(3)]
print(fields)
print(*fields)

print('  0 1 2')
for i in range(len(fields)):
   print(str(i), *fields[i])

