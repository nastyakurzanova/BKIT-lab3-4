from random import randint


# который последовательно выдает заданное количество случайных чисел в заданном диапазоне
# от минимума до максимального, включая диапазоны границ

# любая функция с yield - генератор. При повторном вызове будет продолжаться с yield
def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield randint(begin, end)


if __name__ == '__main__':
    for i in gen_random(15, 1, 100):
        print(i)
