class Problem7(object):

    def __init__(self):
        self.primes = []

    def is_prime(self, num):
        # Assume number is prime until shown it is not.
        isPrime = True
        if num == 0 or num == 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
        return isPrime


    def aggregate_primes(self, num):
        count = 0
        while len(self.primes) < num:
            if self.is_prime(count) == True:
                self.primes.append(count)
            count += 1
        return self.primes[num-1]
