import unittest
import problem_7

class Test7(unittest.TestCase):

    def test_aggregate_6_prime_numbers(self):
        m = problem_7.Problem7()
        self.assertEqual(m.aggregate_primes(6), 13)

if __name__ == '__main__':
    unittest.main()

