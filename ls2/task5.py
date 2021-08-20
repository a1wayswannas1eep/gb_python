# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

r_el = int(input("Введите новый элемент рейтинга: "))
r_list = [7, 5, 3, 3, 2]
a = r_list.count(r_el)
for r in r_list:
    if a > 0:
      b = r_list.index(r_el)
      r_list.insert(b + a, r_el)
      break
    else:
      if r_el > r:
        c = r_list.index(r)
        r_list.insert(c, r_el)
        break
      elif r_el < r_list[len(r_list) - 1]:
        r_list.append(r_el)
print(r_list)

