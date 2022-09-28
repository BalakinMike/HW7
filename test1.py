a = 'Утка | 1 | шт'
lis = a.split('|')
ing = {}
ing['ingredient_name'] = lis[0]
ing['quantity'] = lis[1]
ing['measure'] = lis[2]

print(ing)