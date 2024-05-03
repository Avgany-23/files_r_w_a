import codecs
from pprint import pprint

with codecs.open('recipe.txt', 'r', 'utf') as file:
    a = file.readlines()
    list_recipe = []
    dish = []
    for i, element in enumerate(a):
        element = element.strip()
        if element:
            dish.append(element)

        if not element or i == len(a) - 1:
            list_recipe.append(dish[:])
            dish.clear()

    cook_book = {}
    for element in list_recipe:
        list_dish = []
        for i in element[2:]:
            list_dish.append({'ingredient_name': i[:i.find(' |')], 'quantity': i[i.find('|') + 2:i.rfind(' |')], 'measure': i[i.rfind('| ') + 2:]})
        cook_book[element[0]] = list_dish



del cook_book['Фахитос']
pprint(cook_book, sort_dicts=False, indent=2, width=150)
