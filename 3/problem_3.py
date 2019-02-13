class Problem3(object):

    def __init__(self):
        self.primes = []

    def is_prime(self, num):
        div_count = 0
        count = num
        # Initial check for numbers 0 and 1
        if num == 0 or num == 1:
            return False
        else:
            # Looping backwards
            while count > 0:
                # if number is divisible by current number
                if num % count == 0:
                    # Add to divisible count
                    div_count += 1
                count -= 1
        # If divider count is more than 2, return false
        if div_count > 2:
            return False
        # Else if number can only be divisble by itself and 1
        elif div_count == 2:
            return True

    def aggregate_primes(self, num):
        count = 0
        while count <= num:
            if self.is_prime(count) == True:
                self.primes.append(count)
            count += 1
        return self.primes

    def prime_factors(self, num):
        factors = []
        remain = num
        for n in self.primes:
            while remain % n == 0:
                factors.append(n)
                remain = remain / n
        return factors