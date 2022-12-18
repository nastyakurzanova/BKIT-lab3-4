#-*- coding: cp1251 -*-
import json
from operator import concat
from unique import Unique
from field import field
from gen_random import gen_random

# должна вывести отсортированный список профессий без повторений
def f1(a):
    return Unique([i['job-name'] for i in field(data, 'job-name')], ignore_case=True)

# lambda - анонимные функции без названия, используются один раз
# Принимает в качестве аргументов функцию и последовательность, которую необходимо отфильтровать
# должна фильтровать входной массив и возвращать только те элементы, которые начинаются со слова “программист”
def f2(a):
    return filter(lambda a: a.startswith('программист'), a)

# concat - соединение двух строк
# map применяет к каждому элементу списка переданную функцию
# должна модифицировать каждый элемент массива, добавив строку “с опытом Python”
def f3(a):
    return list(map(lambda x: concat(x, ' c опытом Python'), a))

# zip - объединяет элементы из нескольких источников данных
# должна сгенерировать для каждой специальности зарплату от 100 000 до 200 000 рублей
# и присоединить её к названию специальности
def f4(a):
    return zip(a, gen_random(len(a), 137287, 200000))


with open('data_light.json', 'r', encoding="utf-8-sig") as f:
    data = json.loads(f.read())
    for i in f4(f3(f2(f1(data)))):
        print(i)
