# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
end = []

with open("test4.txt", "r") as my_file:
    for line in my_file:
        end.append(line)

for i, new in enumerate(end):
    words = new.split(' ')
    for n, word in enumerate(words):
        if word in rus:
            words[n] = rus[word].capitalize()
    end[i] = " ".join(words)

with open("test4.1.txt", "w") as result:
    for new in end:
        result.write(new)
