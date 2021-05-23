#!E:\Учёба\Программирование\Python\Курс Stepic\tests\venv\Scripts python
# -*- coding: utf-8 -*-

def read_file(path):
    data = []
    with open(path, "r") as f:
        for s in f:
            data.append(s.strip())
    return data

def write_file(path, data):
    with open(path, "w") as f:
        for i in data:
            f.write(i + "\n")
    return 0


def decode(str):
    '''
    расшивровываем строку в виде a1b2c3,
    где цифра это числе повторений буквы,
    стоящей перед ней
    :param str: строка в виде a1b2c3
    :return: декодированную строку
    '''
    indexs = []
    slice = []
    num = ''
    decode_string = ''
    # ищем индексы всех букв
    for i in range(len(str)):
        if str[i].isalpha():
            indexs.append(i)
    indexs.append(len(str))
    # получаем срезы букв с их числом
    for i in range(1, len(indexs)):
        slice.append(str[indexs[i - 1]:indexs[i]])
    # дальнейшем индексы мне не понадобятся,
    # так что использую переменную для других нужд
    # в целях экономии памяти
    indexs.clear()
    # по каждому срезу
    for str in slice:
        # по каждому символу в срезе
        for i in str:
            # если цифра, составляю полное числло
            if i.isdigit():
                num += i
        indexs.append(int(num))
        num = ''        # не забыть обнулить вспомогательную переменную
    for i in range(len(slice)):
        decode_string += slice[i][0] * indexs[i]
    return decode_string

if __name__ == '__main__':
    path = "dataset_decode_string.txt"
    data = []
    str = read_file(path)
    for i in str:
        data.append(decode(i))
    write_file("decode.txt", data)
