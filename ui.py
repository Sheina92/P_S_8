from logger import input_data, print_data, delete_data, change_data

def interface():
    print("Добрый день! Вы попали на специальный бот-справочник! \n 1 - Добавление данных \n 2 - Редактирование данных \n 3 - Удаление данных \n 4 - Вывод данных \n 5 - Выход")
    command = int(input('Введите число: '))

    while command < 1 or command >= 6:
        print("Неправильный ввод")
        command = int(input('Введите число: '))
    if command == 1:
        input_data()
    elif command == 2:
        change_data()
    elif command == 3:
        delete_data() 
    elif command == 4:
        print_data()
    elif command == 5:
        print('До свидания!')