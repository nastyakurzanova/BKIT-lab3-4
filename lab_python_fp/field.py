# list, который содержит в себе dict
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green', 'amount': 256},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black', 'amount': 102},
    {'title': 'Стол маленький', 'price': 2700, 'color': 'white', 'amount': 53},
    {'title': 'Ваза для цветов', 'price': 1590, 'color': 'blue', 'amount': 96},
    {'title': 'Кресло', 'price': 3000, 'color': 'red', 'amount': 100},
]

# В качестве первого аргумента генератор принимает список словарей,
# дальше через *args генератор принимает большое количество аргументов.
# *args **kwargs


# первый аргумент словарь
def field(items, *args):
    try:
        # assert проверка, является ли условие истинным
        assert len(args) > 0
        # Заполняем список пустыми словарями
        # for в одну строку
        r = [{} for i in range(len(items))]
        for i in range(len(items)):
            for key in items[i]:
                if key in args:
                    r[i].update({key: items[i][key]})
        return r
    except:
        print("Ничего не передали")


if __name__ == '__main__':
    for i in field(goods, 'title', 'price'):
        print(i)

