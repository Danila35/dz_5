"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit

from collections import OrderedDict as o_dict

dict_for_test_one = {str(i): i for i in range(1000)}
dict_for_test_two = {str(i): i for i in range(100000, 101000)}

o_dict_for_test_one = o_dict(dict_for_test_one)

o_dict_for_test_two = o_dict(dict_for_test_two)


def filling_dict(num):
    a = dict()
    for i in range(num):
        a[str(i)] = i


def filling_o_dict(num):
    a = o_dict()
    for i in range(num):
        a[str(i)] = i


def for_every_kv_dict(filled_dict):
    for key, value in filled_dict.items():
        a = key
        b = value


def for_every_kv_o_dict(filled_dict):
    for key, value in filled_dict.items():
        a = key
        b = value


def list_sorting_dict(filled_dict):
    a = sorted(filled_dict.items(), key=lambda item: item[1])


def list_sorting_o_dict(filled_dict):
    a = sorted(filled_dict.items(), key=lambda item: item[1])


def popitem_dict(filled_dict):
    for i in range(len(filled_dict)):
        a = filled_dict.popitem()


def popitem_o_dict(filled_dict):
    for i in range(len(filled_dict)):
        a = filled_dict.popitem()


def get_dict(filled_dict):
    for i in range(len(filled_dict)):
        filled_dict.get(str(i))


def get_o_dict(filled_dict):
    for i in range(len(filled_dict)):
        filled_dict.get(str(i))


def update_dict(filled_dict_one, filled_dict_two):
    filled_dict_one.update(filled_dict_two)


def update_o_dict(filled_dict_one, filled_dict_two):
    filled_dict_one.update(filled_dict_two)


name_list = 'filling_dict filling_o_dict for_every_kv_dict ' \
            'for_every_kv_o_dict list_sorting_dict list_sorting_o_dict ' \
            'popitem_dict popitem_o_dict get_dict get_o_dict update_dict ' \
            'update_o_dict'.split()

num_time = 10000

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print()
    if id == 0 or id == 1:
        print(f"{func_name} -",
              timeit(stmt=func_name + f'(1000)',
                      number=num_time, globals=globals()))

    elif id == 10:
        print(
            f"{func_name} -",
            timeit(stmt=func_name + f'(dict_for_test_one.copy(), '
                    f'dict_for_test_two.copy())',
                    number=num_time, globals=globals()))
    elif id == 11:
        print(
            f"{func_name} -",
            timeit(stmt=func_name + f'(o_dict_for_test_one.copy(), '
                    f'o_dict_for_test_two.copy())',
                    number=num_time, globals=globals()))
    else:
        if id % 2 == 0:
            print(
                f"{func_name} -",
                timeit(stmt=func_name + f'(dict_for_test_one.copy())',
                        number=num_time, globals=globals()))
        else:
            print(
                f"{func_name} -",
                timeit(stmt=func_name + f'(o_dict_for_test_one.copy())',
                        number=num_time, globals=globals()))

"""
Видно что OrderedDict работает несколько медленнее чем обычный словарь
и словарь на версии python 3.6 и выше лучше оптимихирован поэтому OrderedDict не нужен на этих версиях
filling_dict - 2.5132335
filling_o_dict - 2.8214143

for_every_kv_dict - 0.36618880000000065
for_every_kv_o_dict - 1.7459799

list_sorting_dict - 1.1434208000000003
list_sorting_o_dict - 2.5497109999999985

popitem_dict - 0.8084121999999994
popitem_o_dict - 2.5121008000000007

get_dict - 2.5067771999999984
get_o_dict - 3.396056899999998

update_dict - 0.5006723999999991
update_o_dict - 3.655009500000002
"""