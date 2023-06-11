"""В папке есть 4 файла. 1.txt, 2.txt, 3.txt - содержат текст,
Файл result.txt изначально пустой. После заверщения программы
в нем будет сохранен результат первых трех файлов."""

files_list = ['1.txt', '2.txt', '3.txt']   # Создаем список с названиями всех файлов
files_dict ={}                             # Создаем словарь для добавления названия файла: количество строк
numbers_list = []                          # Создаем список, чтобы отсортировать количество строк

for file in files_list:
    with open(file, 'r', encoding='utf-8') as f:
        tmp = f.readlines()
        result = len(tmp)
        files_dict.setdefault(file, result)
        numbers_list.append(result)

numbers_list.sort(reverse=True)
keys_list = list(files_dict.keys())

for value in numbers_list:
    index = list(files_dict.values()).index(value)   # Находим нужный индекс в словаре по значению value
    keys_list = list(files_dict.keys())
    with open(keys_list[index], 'r', encoding='utf-8') as input_file, open('result.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(keys_list[index] + '\n')
        output_file.write(str(value) + '\n')
        output_file.writelines(input_file)
        output_file.write('\n')

print('Файлы отсортированы и записаны в result.txt')
