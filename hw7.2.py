

from itertools import count


def inspect_file(text_file): # 
    with open(text_file, encoding='utf-8') as file:
        n = len(file.readlines())
    return (n)

def read_write(t_file, key):
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

list_file = {}
len_file = inspect_file('1.txt')
list_file[len_file] = '1.txt'
len_file = inspect_file('2.txt')
list_file[len_file] = '2.txt'
len_file = inspect_file('3.txt')
list_file[len_file] = '3.txt'
print(list_file)
count_key = list(list_file.keys())
count_key.sort()
print(count_key)
for key in count_key:
    read_write(list_file[key], key)