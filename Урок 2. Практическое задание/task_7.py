"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
Правой части в рекурсии быть не должно. Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s += i
# m = n * (n + 1) // 2
# print(s)
# print(m)


def get_sum_by_recursion(number: int, sum_by_recursion=0):
    """ Рекурсивно считает сумму чисел от 1 до number, где number - натуральное число """
    if number == 1:
        return sum_by_recursion + 1
    sum_by_recursion += number
    number -= 1
    return get_sum_by_recursion(number, sum_by_recursion)


def get_sum_by_formula(number: int):
    return number * (number+1) / 2


sum_by_recur = get_sum_by_recursion(5)
sum_by_formula = get_sum_by_formula(5)
print(f'{sum_by_recur == sum_by_formula}')
