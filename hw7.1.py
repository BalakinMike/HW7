

def cook_books(recept):
    with open(recept, encoding='utf-8') as file:
        cook_book = {} 
        for line in file:
            dish_name = line.strip()
            ingredients_num = file.readline().strip()
            ingredients = []
            for car in range(int(cars_numbers)):
                cars_list.append(file.readline().strip())
            report[shop_name] = cars_list
            file.readline()

# from pprint import pprint
# pprint(report)



cook_books('recept.txt')