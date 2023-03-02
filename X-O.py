print("Приветствую в игре Крестики-нолики (X-O)!")

#Начальная установка полей для ввода данных
fields = [['-']*3 for _ in range(3)]

#Приводим поле в адекватный внешний вид
def show_fields(f):
    print('  0 1 2')
    for i in range(len(fields)):
        print(str(i)+' '+' '.join(fields[i]))
show_fields(fields)

#Задаем вопрос по координатам для ввода координат:
def users_input(f):
    while True:
        place=input("Введите координаты для поля:").split()
        if len(place) != 2:
            print('Необходимо ввести две координаты')
            continue
        
    
        if not(place[0].isdigit() and place[1].isdigit()):
            print("Введите числа")
            continue
        
        x,y = map(int, map)
        
        
        
        
        break
    return place

users_input(fields)