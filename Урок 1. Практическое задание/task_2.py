"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""


def search_min_slow(income_list):
    """
        Возвращает минимальное значение в списке, сравнивая каждый элемент с каждым другим
        Работает с данными одного типа; если список пустой, то возвращает None
        Сложность алгоритма: O(n^2) - квадратичная.
    """
    if not income_list:  # O(1)
        return None  # O(1)
    min_value = income_list[0]  # O(1)
    for i in range(len(income_list) - 1):  # O(len(lst) - 1)
        for j in range(1, len(income_list)):  # O(len(lst) - 1)
            if income_list[j] < income_list[i] and income_list[j] < min_value:  # O(1) + O(1)
                min_value = income_list[j]  # O(1)
    return min_value  # O(1)


def search_min_fast(lst):
    """
        Возвращает минимальное значение в списке, выбирая минимальное значение (однопроходный)
        Работает с данными одного типа и не пустым списком
        Сложность алгоритма: O(n) - линейная
    """
    min_value = lst[0]
    try:
        for i in range(1, len(lst)):
            if lst[i] < min_value:
                min_value = lst[i]
        return min_value
    except TypeError:
        print('Некорректный список')


print(search_min_fast([1, 6, -2, 3, 7, 0]))
print(search_min_fast([('n1ds', 'a2'), ('a3', 'r7', 'n')]))

print(search_min_slow([1, 6, -2, 3, 7, 0]))
print(search_min_slow([('n1ds', 'a2'), ('a3', 'r7', 'n')]))
print(search_min_slow([]))
