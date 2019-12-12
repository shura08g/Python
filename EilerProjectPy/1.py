'''
http://www.s-anand.net/euler.html
Задача 1
Числа, кратные 3 или 5

Если выписать все натуральные числа меньше 10, кратные 3 или 5,
то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

limit = 1000


def eiler1():
    summa = 0
    i = 3
    while (i <= limit):
        if ((i % 3) == 0 or (i % 5) == 0):
            summa += i
        i += 1
    print("#1. Sum = {}".format(summa))


if __name__ == "__main__":
    eiler1()  # 234168
