
class Prob10(object):

    def __init__(self):
        self.primes = []

    def create_primes(self, num):
        for possiblePrime in range(2, num + 1):

            # Assume number is prime until shown it is not.
            isPrime = True
            for num in range(2, int(possiblePrime ** 0.5) + 1):
                if possiblePrime % num == 0:
                    isPrime = False
                    break
            if isPrime:
                self.primes.append(possiblePrime)
        return self.primes

    def sum_of_primes(self, num):
        self.create_primes(num)
        totals = 0
        for i in self.primes:
            totals += i
        return totals