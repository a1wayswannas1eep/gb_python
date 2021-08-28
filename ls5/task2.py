# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open("test2.txt", "a")

if my_file.writable():
    sl = [')\n', '123\n', '12345\n']
    my_file.writelines(sl)

my_file = open("test2.txt", "r")
lines = my_file.readlines()
print(f"Колличество строк: {len(lines)}")
my_file = open("test2.txt", "r")
words = my_file.readlines()
for i in range(len(words)):
    line = words[i].split()
    word = len(line)
    print(f"Колличество слов в строке: {word} в строке: {i}")

my_file.close()
