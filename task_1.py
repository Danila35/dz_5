"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""


from collections import namedtuple

def enterpises():
    num = int(input("Введите количество предприятий: "))
    Companies = namedtuple("company", "name period_1 period_2 period_3 period_4")
    total_profit = 0
    for i in range(num):
        company = Companies(
            name=input("Введите название предприятия: "),
            period_1=int(input("Введите прибыль за 1-й квартал: ")),
            period_2=int(input("Введите прибыль за 2-й квартал: ")),
            period_3=int(input("Введите прибыль за 3-й квартал: ")),
            period_4=int(input("Введите прибыль за 4-й квартал: ")))

    total_average = {}
    total_average[company.name] = (company.period_1 + company.period_2 + company.period_3 + company.period_4) / 4

    for profit in total_average.values():
        total_profit += profit

    average = total_profit / num

    print(f'Средняя прибыль = {total_average}')

    for firm, profit in total_average.items():
        if profit > average:
            print(f"Предприятия, с прибылью выше среднего значения: {firm}")
        elif profit < average:
            print(f"Предприятия, с прибылью ниже среднего значения: {firm}")
        else:
            print("Их прибыль равна")

enterpises()