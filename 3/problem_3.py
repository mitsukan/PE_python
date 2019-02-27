class Problem3(object):

    def __init__(self):
        self.primes = []

    def is_prime(self, num):
        # Assume number is prime until shown it is not.
        isPrime = True
        if num == 0 or num == 1:
            return False
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                isPrime = False
                break
        return isPrime

    def aggregate_primes(self, num):
        for possiblePrime in range(2, num + 1):
            if self.is_prime(possiblePrime) == True:
                self.primes.append(possiblePrime)
        return self.primes

    def prime_factors(self, num):
        factors = []
        remain = num
        for n in self.primes:
            while remain % n == 0:
                factors.append(n)
                remain = remain / n
        return factors