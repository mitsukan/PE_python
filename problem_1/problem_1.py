def problem_1(num):
    total = 0
    count = num
    while count > 0:
        count -= 1
        if count % 3 == 0:
            total += count
        elif count % 5 == 0:
            total += count
        print('printing count: {}'.format(count))
        print('printing total: {}'.format(total))
    return total
