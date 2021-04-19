"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from collections import deque
from timeit import timeit

list_with_range = [el for el in range(1000)]
deque_with_range = deque()
deque_with_range.extend(list_with_range)


def list_append(num):
    my_list = []
    for i in range(num):
        my_list.append(i)


def deque_append(num):
    my_list = deque()
    for i in range(num):
        my_list.append(i)


def list_appendleft(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def deque_appendleft(num):
    my_list = deque()
    for i in range(num):
        my_list.appendleft(i)


def list_extend(lst_range):
    my_list = []
    my_list.extend(lst_range)


def deque_extend(lst_range):
    my_list = deque()
    my_list.extend(lst_range)


def list_extendleft(lst_range):
    my_list = []
    for el in lst_range:
        my_list.insert(0, el)


def deque_extendleft(lst_range):
    my_list = deque()
    my_list.extendleft(lst_range)


def list_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def deque_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def list_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop(0)


def deque_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.popleft()


def list_reverse(lst_range):
    a = lst_range.reverse()


def deque_reverse(lst_range):
    a = lst_range.reverse()


name_list = 'list_append deque_append list_appendleft deque_appendleft' \
            ' list_extend deque_extend list_extendleft deque_extendleft ' \
            'list_pop deque_pop list_popleft deque_popleft ' \
            'list_reverse deque_reverse'.split()

num_time = 10000

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print()
    if id <= 3:
        print(
            f"{func_name} -",
            timeit(stmt=func_name + f'(1000)',
                   number=num_time,
                   globals=globals()))
    else:
        if id % 2 == 0:
            print(
                f"{func_name}(list_with_range.copy()) -",
                timeit(stmt=func_name + f'({list_with_range})',
                       number=num_time,
                       globals=globals()))
        else:
            print(
                f"{func_name}(deque_with_range.copy()) -",
                timeit(stmt=func_name + f'({deque_with_range})',
                       number=num_time,
                       globals=globals()))

"""Аналитика
deque в appendleft, extendleft, popleft принимает O (1) и был оптимизирован под это же
в случае с list то он принимает O (n)
в обычных же случая deque (append, extend pop) работает почти на той же скорости
но есть исключение в виде reverse, у меня работает чуть ли не в 10 раз медленней

list_append - 0.5336808
deque_append - 0.4832434

list_appendleft - 3.1209828999999996
deque_appendleft - 0.48891940000000034

list_extend(list_with_range.copy()) - 0.06567159999999994
deque_extend(deque_with_range.copy()) - 0.2158736000000001

list_extendleft(list_with_range.copy()) - 3.0097927
deque_extendleft(deque_with_range.copy()) - 0.1951893000000009

list_pop(list_with_range.copy()) - 0.5029272000000002
deque_pop(deque_with_range.copy()) - 0.48861940000000104

list_popleft(list_with_range.copy()) - 1.8642581000000007
deque_popleft(deque_with_range.copy()) - 0.6272832000000008

list_reverse(list_with_range.copy()) - 0.03895520000000019
deque_reverse(deque_with_range.copy()) - 0.145642500000001

"""