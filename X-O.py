print("Приветствую в игре Крестики-нолики (x-o)!")

#Начальная установка полей для ввода данных
fields = [['-']*3 for _ in range(3)]

#Приводим поле в адекватный внешний вид
def show_fields(f):
    print('  0 1 2')
    for i in range(len(fields)):
        print(str(i)+' '+' '.join(fields[i]))
show_fields(fields)

#Задаем вопрос по координатам для ввода:
def users_input(f):
    while True:
        place=input("Введите координаты для поля:").split()
        if len(place) != 2:
            print('Необходимо ввести две координаты')
            continue
        
    
        if not(place[0].isdigit() and place[1].isdigit()):
            print("Введите числа")
            continue
        
        x,y = map(int, place)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print("Вы вышли из диапазона")
            continue
        
        if f[x][y] != '-':
            print("Клетка занята")
            continue
        
        break
    return place

users_input(fields)


#Показываем, что получается, пользователю
fields=[['-']*3 for _ in range(3)]
count=0
while True:
    if count==9:
        print('Ничья')
        break
    if count%2 == 0:
        user='x'
    else:
        user='o'
        
    show_fields(fields)
    x,y = users_input(fields)
    fields[x][y] = user
    count += 1
