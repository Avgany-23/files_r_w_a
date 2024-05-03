import pprint


# Из первого задания, без последнего рецепта. Изменил рецепты для проверки (когда повторяются ингредиенты)
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 500, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Яйцо', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):
    dict_ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ing = ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
            if dict_ingredients.get(ing[0]) is None:
                dict_ingredients.setdefault(*ing)
                continue
            dict_ingredients[ingredient['ingredient_name']]['quantity'] = dict_ingredients[ing[0]]['quantity'] + ingredient['quantity'] * person_count

    return dict_ingredients

pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))