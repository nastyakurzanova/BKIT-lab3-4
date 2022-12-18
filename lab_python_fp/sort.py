data = [4, -30, 100, -100, 123, 1, 0, -1, -4]


if __name__ == '__main__':
    # reverse=true в обратном порядке
    result = sorted(data, key=abs, reverse=True)
    print(result)
    result_with_lambda = sorted(data, key=lambda a: -abs(a))
    print(result_with_lambda)
    ss = lambda b: sorted(b, key=abs, reverse=True)
    print(ss(data))
