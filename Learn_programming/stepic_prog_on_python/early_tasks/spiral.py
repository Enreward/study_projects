#coding: utf-8

def spiral(n):
    '''
    Выводит в консоль числа от 1 до n^2 по спирали
    :param n: челое число
    :return:
    '''
    matrix = [[0 for k in range(n)] for l in range(n)]
    i, j = 0, 0
    top_wall = 0
    left_wall = 0
    right_wall = n -1
    bot_wall = n -1
    e = 0

    # Проходим по виткам спирали
    for p in range(n//2+1):
        # Движемся вправо пока не упрёмся в стену
        while j < right_wall:
            e += 1
            matrix[i][j] = e
            j += 1
        top_wall += 1
        # Движемся вниз пока не упрёмся в стену
        while i < bot_wall:
            e += 1
            matrix[i][j] = e
            i += 1
        right_wall -= 1
        # Движемся влево пока не упрёмся в стену
        while j > left_wall:
            e += 1
            matrix[i][j] = e
            j -= 1
        bot_wall -= 1
        # Движемся вверх пока не упрёмся в стену
        while i > top_wall:
            e += 1
            matrix[i][j] = e
            i -= 1
        left_wall += 1
    # Центральный элемент
    matrix[i][j] = n**2

    for i in range(n):
        string = ''
        for j in range(n):
            string += (str(matrix[i][j]) + ' ')
        print(string)

n = int(input())
spiral(n)
