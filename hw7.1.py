
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
    
    for i in dishes:
        for j in range (0, len(cook_book[i])):
            n_ing = {}
            if (cook_book[i][j]['ingredient_name']) not in numb_ingridients:
                n_ing['quantity'] = int(cook_book[i][j]['quantity'])*person_count
                n_ing['measure'] = cook_book[i][j]['measure']
                numb_ingridients[cook_book[i][j]['ingredient_name']] = n_ing
            else:
                n_ing['quantity'] = int(cook_book[i][j]['quantity'])*person_count + int(cook_book[i][j]['quantity'])*person_count
                n_ing['measure'] = cook_book[i][j]['measure']
                numb_ingridients[cook_book[i][j]['ingredient_name']] = n_ing
    pprint(numb_ingridients)
        
    return
#cook_books('recept.txt')
cook_book = cook_books('recept.txt')
from pprint import pprint
pprint(cook_book)


# Формирование запроса на нужные блюда
dishes = []
dish = ' '
while dish != '':
    dish = input('Введите желаемое блюдо (соблюдая формат названия из кулинарной книги). Конец заказа - пустой ввод: ')
    if dish in cook_book:
        dishes.append(dish)
    else:
        if dish != '':
            print('Введенное блюдо отсутствует в кулинарной книге')

person_count = int(input('Введите количество гостей: '))
get_shop_list_by_dishes(cook_book, dishes, person_count)
#print(dishes)
#print(cook_book['Омлет'][1]['ingredient_name'])
#cook_books('recept.txt')