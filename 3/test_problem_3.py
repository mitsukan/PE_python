import unittest
import problem_3

class Test3(unittest.TestCase):

    def test_is_prime_number(self):
        newprob = problem_3.Problem3()
        self.assertEqual(newprob.is_prime(2), True)
        self.assertEqual(newprob.is_prime(3), True)
        self.assertEqual(newprob.is_prime(5), True)
        self.assertEqual(newprob.is_prime(23), True)

        self.assertEqual(newprob.is_prime(4), False)
        self.assertEqual(newprob.is_prime(9), False)
        self.assertEqual(newprob.is_prime(15), False)
        self.assertEqual(newprob.is_prime(1), False)
        self.assertEqual(newprob.is_prime(86), False)

    def test_prime_aggregator(self):
        newprob = problem_3.Problem3()
        self.assertEqual(newprob.aggregate_primes(23),[2,3,5,7,11,13,17,19,23])

    def test_prime_aggregator2(self):
        newprob = problem_3.Problem3()
        self.assertEqual(newprob.aggregate_primes(109), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109])

    def test_prime_factor(self):
        newprob = problem_3.Problem3()
        newprob.aggregate_primes(228)
        self.assertEqual(newprob.prime_factors(228), [2,2,3,19])

    def test_prime_factor2(self):
        newprob = problem_3.Problem3()
        newprob.aggregate_primes(200)
        self.assertEqual(newprob.prime_factors(13195), [5,7,13,29])

    def test_problem_solver(self):
        n = problem_3.Problem3()
        n.aggregate_primes(int(600851475143**0.5))
        print('solution to problem 3...')
        print(n.prime_factors(600851475143))

if __name__ == '__main__':
    unittest.main()
