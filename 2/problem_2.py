class Problem2(object):

    def __init__(self):
        self.fib_seq = []

    def fibonacci(self, num):
        count1 = 1
        count2 = 2
        self.fib_seq = [1,2]
        while count2 < num:
            next = count1 + count2
            self.fib_seq.append(next)
            count1 = count2
            count2 = next
        return self.fib_seq

    def solver(self, num):
        total = 0
        for term in self.fib_seq:
            if term % 2 == 0:
                total += term
            if term == num:
                break
        return total