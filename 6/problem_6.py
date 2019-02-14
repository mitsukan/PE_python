def sum_of_squares(num):
    l = list(range(1, num + 1))

    for index, number in enumerate(l):
        l[index] = number ** 2
    return sum(l)


def square_of_sum(num):
    l = list(range(1, num + 1))
    return sum(l) ** 2

