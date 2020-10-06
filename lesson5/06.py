"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""
import json
profit = {}
profit1 = {}
profit2 = 0
average_profit = 0
i = 0
with open('06.txt', 'r') as my_file:
    for line in my_file:
        name, company, profed, loss = line.split()
        profit[name] = int(profed) - int(loss)
        if profit.setdefault(name) >= 0:
            profit2 = profit2 + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = profit2 / i
        print(f"Средняя прибыль - {average_profit:.2f}")
    else:
        print(f"Прибыль средняя отсутствует. Компании работают в убыток")
    profit1 = {'Средняя прибыль': round(average_profit)}
    profit.update(profit1)
    print(f'Прибыль каждой компании - {profit1}')

with open('file_07.txt', 'w') as new_file:
    json.dump(profit, new_file)

    js_string = json.dumps(profit)
    print(f'Создан json файл с содержанием \n' f'{js_string}')
