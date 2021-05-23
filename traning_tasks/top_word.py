#!E:\Учёба\Программирование\Python\Курс Stepic\tests\venv\Scripts python
# -*- coding: utf-8 -*-

def read_file(path):
    with open(path, "r") as f:
        str = f.read()
    print(str)
    return str

def write_file(path, data):
    with open(path, "w") as f:
        f.write(data + "\n")
    return 0

def selektion_sort(data):
    '''
    Сортировка выборкой
    Выбрал эту по причине простоты понимания, а так же
    не видел надобности писать громоздкую сортировку слиянием или быструю
    :param data:
    :return:
    '''
    # проходим по всему массиву до предпоследнего
    for i in range(len(data)-1):
        # на каждой итерации выбираем индекс текущего элемента как наибольший
        bigger_value_index = i
        # со следующего до последнего элемента ищем наибольший
        for j in range(i+1, len(data)):
            # запоминаем индекс наибольшего
            if data[j] > data[bigger_value_index]:
                bigger_value_index = j
        # меняем местами текущий и наибольший
        data[i], data[bigger_value_index] = data[bigger_value_index], data[i]

def top_word(data):
    '''
    Поиск самого популярного слова в тексте
    :param data: непрерывная строка с исходным текстом
    :return: строку: <популярное_слово> <число_его_повторений>
    '''
    # убираем пробельные символы в начале и конце строки
    # переводим в нижний регистр и делим строку по пробелам
    data = data.strip().lower().split()
    words = {}      # словарь слов и их количества
    top = []        # список популярных слов
    # проходим по массиву слов из текста
    for s in data:
        # если слово есть в словаре, увеличиваем его число на 1
        if s in words:
            words[s] += 1
        # иначе создаём элемент словаря с единичным числом
        else:
            words[s] = 1
    # сортируем список из кооличества слов
    counts = [i for i in words.values()]
    selektion_sort(counts)      # сортируем
    # получаем список всех популярных слов
    for k in words.keys():
        if words[k] == counts[0]:
            top.append(k)
    # перебираем список популярных слов чтобы найти лексикографически первейшее
    most_top = top[0]
    for s in top:
        if s < most_top:
            most_top = s
    return most_top + ' ' + str(words[most_top])


if __name__ == "__main__":
    string = read_file("dataset_top_word.txt")
    most_top_word = top_word(string)
    write_file("most_top_word.txt", most_top_word)
