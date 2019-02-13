import unittest
import problem_3

class Test3(unittest.TestCase):

    def test_calculates_prime_number(self):
        newprob = problem_3.Problem3()
        self.assertEqual(newprob.cal_prime(23), [2,3,5,7,11,13,17,19,23])


if __name__ == '__main__':
    unittest.main()
