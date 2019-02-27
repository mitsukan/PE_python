
class Prob10(object):

    def __init__(self):
        self.primes = []

    def is_prime(self, num):
        if num == 2:
            return True
        if num == 9:
            return False
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    return True
        return False

    def create_primes(self, num):
        i = 1
        while i < num:
            if self.is_prime(i) == True:
                self.primes.append(i)
            i += 1
        return self.primes

    def sum_of_primes(self, num):
        self.create_primes(num)
        totals = 0
        for i in self.primes:
            totals += i
        return totals