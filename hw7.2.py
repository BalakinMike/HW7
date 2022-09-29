

from itertools import count


def inspect_file(text_file): # Процедура подсчёта длины файлов
    with open(text_file, encoding='utf-8') as file:
        n = len(file.readlines())
    return (n)

def read_write(t_file, key):# Процедура чтения файла и записи информации в общий файл
    with open(t_file, 'r', encoding='utf-8') as file_read, open(r'final_file.txt', 'a', encoding='utf-8') as file_write:
            num = str(key)
            file_write.write(t_file)
            file_write.write('\n')
            file_write.write(num)
            file_write.write('\n')
            for line in file_read:
                file_write.write(line)
            file_write.write('\n')
    return

work_list = ['1.txt', '2.txt', '3.txt'] # Список названий файлов для обработки
list_file = {} # Словарь ключ - число строк, значение  - название файла
for work_file in work_list:
    len_file = inspect_file(work_file)
    list_file[len_file] = work_file

count_key = list(list_file.keys()) # сортировка ключей по возрастанию 
count_key.sort()
for key in count_key:
    read_write(list_file[key], key)