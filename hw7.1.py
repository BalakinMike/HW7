
def vocabular_ingridients(components): # Создание словаря одного компонента
    lis = components.split('|') #Список из строки
    ing = {}
    ing['ingredient_name'] = lis[0]
    ing['quantity'] = lis[1]
    ing['measure'] = lis[2]
    return ing


def cook_books(recept): # Формирование кулинарной книги
    with open(recept, encoding='utf-8') as file:
        cook_book = {} 

        for line in file:
            dish_name = line.strip()
            ingredients_num = file.readline().strip()
            ingredients = []
            
            for ingridient in range(int(ingredients_num)):
                components = (file.readline().strip())
                ingredients.append(vocabular_ingridients(components))
            cook_book[dish_name] = ingredients
            file.readline()
    return (cook_book)

def get_shop_list_by_dishes(cook_book, dishes, person_count): #Формирование списка ингридиентов
    numb_ingridients = {}
    
    for dish in dishes:
        for j in range (0, len(cook_book[dish])): # Счётчик по количеству ингридиентов
            n_ing = {}
            if (cook_book[dish][j]['ingredient_name']) not in numb_ingridients: # Проверка на повторяемость ингридиентов
                n_ing['quantity'] = int(cook_book[dish][j]['quantity'])*person_count
                n_ing['measure'] = cook_book[dish][j]['measure']
                numb_ingridients[cook_book[dish][j]['ingredient_name']] = n_ing
            else: # Если ингридиент уже существует, то его количество просто увеличивается
                n_ing['quantity'] = int(cook_book[dish][j]['quantity'])*person_count + int(cook_book[i][j]['quantity'])*person_count
                n_ing['measure'] = cook_book[dish][j]['measure']
                numb_ingridients[cook_book[dish][j]['ingredient_name']] = n_ing
    pprint(numb_ingridients)
        
    return

# Основная программа
cook_book = cook_books('recept.txt')
from pprint import pprint
pprint(cook_book) # Вывод всей кулинарной книги


# Формирование запроса на нужные блюда
dishes = []
dish = ' '
while dish != '': # Проверка на конец ввода блюд
    dish = input('Введите желаемое блюдо (соблюдая формат названия из кулинарной книги). Конец заказа - пустой ввод: ')
    if dish in cook_book:
        dishes.append(dish)
    else:
        if dish != '':
            print('Введенное блюдо отсутствует в кулинарной книге')

person_count = int(input('Введите количество гостей: '))
get_shop_list_by_dishes(cook_book, dishes, person_count)
