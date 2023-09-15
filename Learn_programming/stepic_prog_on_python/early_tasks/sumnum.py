def sumnum(n):
    """
    Написать функцию, которая находит сумму всех цифр в числе. На вход также могут пойти и числа меньше нуля — их стоит
    переводить в неотрицательное числа.

    Пример:
    sumnum(1234) → 10
    sumnum(-9876) → 30
    sumnum(7013) → 11
    sumnum(100001) → 2
    :param n: целое число
    :return: сумма цифр числа
    """

    n = str(n).replace('-', '')
    sum_n = sum(list(map(int, n)))
    return sum_n


print(sumnum(1234))
print(sumnum(-9876))
