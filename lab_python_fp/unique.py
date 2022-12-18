class Unique(object):
    # конструктор
    # *args, **kwargs - распаковка
    def __init__(self, items, **kwargs):
        self.r = []
        # по ключу и по значению ищет
        for key, value in kwargs.items():
            if key == 'ignore_case' and value == True:
                try:
                    # Преобразует все символы верхнего регистра в строке в символы нижнего регистра
                    items = [i.lower() for i in items]
                finally:
                    break

        for i in items:
            if i not in self.r:
                # Добавляют в конец
                self.r.append(i)
# переход к следующему значению и его считыванию
    # дает следующий элемент

    def __next__(self):
        try:
            x = self.r[self.begin]
            self.begin += 1
            return x
        except:
            raise StopIteration
# как init Для цикла,инициализация цикла
# __iter__(self) – получение итератора для перебора объекта

    def __iter__(self):
        # объявляется начальный элемент 0
        self.begin = 0
        return self

# Необходимый реализуйтератор Unique(данные),
# который берет на вход массив или генератор и итерируется по элементу, пропуская дубликаты.

if __name__ == '__main__':
    data = [1, 4, 87, 3, 5, 7, 2, 4, 6, 4, 3, 6, 3, 4, 2]
    b = ['A', 'a', 'B', 'b', 'A', 'b', 'c']
    for i in Unique(b):
        print(i)



# a = [1,4,87,3,5,7,2,4,6,4,3,6,3,4,2]
# b = ['A', 'a', 'B', 'b']
# for i in Unique(b, ignore_case=True):
#     print(i)
