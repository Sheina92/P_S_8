from data_create import name_data, surname_data, phone_data, address_data
from tempfile import NamedTemporaryFile
import shutil
import csv

def input_data(): #Ввод данных
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n\n"
    f"Выберите вариант: "))

    while var !=1 and var !=2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        with open('data1.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data2.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
        print("Запись успешно добавлена!")

def change_data(): #Редактирование данных
    var = int(input(f"Какой формат данных редактировать\n\n"
    f"1 Вариант \n"
    f"2 Вариант \n"
    f"Выберите вариант: "))

    while var !=1 and var !=2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    filename = ''
    lines = {}
    print("Выберите номер записи для редактирования: ")
    if var == 1:
        filename = 'data1.csv'
        with open(filename, 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            counter = 1
            j = 0
            for i in range(len(data_first)):
                if data_first[i].isspace() or i == len(data_first) - 1:
                    lines[counter] = ''.join(data_first[j:i+1])
                    counter = counter + 1
                    j = i + 1
    elif var == 2:
        filename = 'data2.csv'
        with open(filename, 'r', encoding='utf-8') as f:
            i = 1
            for line in f.readlines():
                if not line.isspace():
                    lines[i] = f"{line}"
                    i = i + 1

    for key in lines:
        print(f"{key}. {lines[key]}")

    row_number = int(input())
    
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    phone = input("Введите номер телефона: ")
    address = input("Введите адрес: ")

    if var == 1:
        lines[row_number] = f"{name}\n{surname}\n{phone}\n{address}\n\n"
    elif var == 2:
        lines[row_number] = f"{name};{surname};{phone};{address}\n"

    for k, v in list(lines.items()):
        if v.isspace():
            del lines[k]

    with open(filename, 'w', encoding='utf-8') as csvFile:
        text = ''.join(lines.values())
        csvFile.write(text)
        print("Запись успешно изменена!")

  
def delete_data(): #Удаление данных
    var = int(input(f"Какой формат данных удалять\n\n"
                    f"1 Вариант \n"
                    f"2 Вариант \n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    filename = ''
    lines = {}
    print("Выберите номер записи для удаления: ")
    if var == 1:
        filename = 'data1.csv'
        with open(filename, 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            counter = 1
            j = 0
            for i in range(len(data_first)):
                if data_first[i].isspace() or i == len(data_first) - 1:
                    lines[counter] = ''.join(data_first[j:i + 1])
                    counter = counter + 1
                    j = i + 1
    elif var == 2:
        filename = 'data2.csv'
        with open(filename, 'r', encoding='utf-8') as f:
            i = 1
            for line in f.readlines():
                if not line.isspace():
                    lines[i] = f"{line}"
                    i = i + 1

    for key in lines:
        print(f"{key}. {lines[key]}")

    row_number = int(input())

    del lines[row_number]

    for k, v in list(lines.items()):
        if v.isspace():
            del lines[k]

    with open(filename, 'w', encoding='utf-8') as csvFile:
        text = ''.join(lines.values())
        csvFile.write(text)
        print("Запись успешно удалена!")

def print_data(): #Вывод данных
    print('Вывожу данные из 1 файла: \n')
    with open('data1.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))


    print('Вывожу данные из 2 файла: \n')
    with open('data2.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)