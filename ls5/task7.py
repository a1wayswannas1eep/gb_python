# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

c_list = []

with open("test7.txt", "r") as my_file:
    for i in my_file:
        c_list.append(i.replace("\n", ""))

comps = {}
plus = []
minus = {}

for comp in c_list:
    company = [info for info in comp.split(" ")]
    if len(company) > 4:
        company = [" ".join(company[:-3]), company[-3], company[-2], company[-1]]
    company_name = company[0]
    company_p = int(company[-2])
    company_m = int(company[-1])
    company_profit = company_p - company_m
    comps[company_name] = company_profit
    if company_profit >= 0:
        plus.append(company_profit)

try:
    minus["Average profit"] = round(sum(plus)/len(plus), 2)
except ZeroDivisionError:
    minus["Average profit"] = 0

final_list = [comps, minus]

with open("companies.json", "w") as json_file:
    json.dump(final_list, json_file)
