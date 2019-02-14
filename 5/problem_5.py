from itertools import permutations

def example(min, max):
    l = list(map(list, permutations(range(min,max), 10)))
    possibility = 2000

    while possibility > 100:
        for perm in l:
            answer = possibility
            for i in perm:
                answer /= i
            if answer % 1 == 0:
                print(possibility)
                return possibility


        possibility += 1