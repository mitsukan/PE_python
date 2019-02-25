import unittest
import problem_10

class Test10(unittest.TestCase):

    def test_can_test_a_prime(self):
        n = problem_10.Prob10()
        self.assertEqual(n.is_prime(5), True)





if __name__ == '__main__':
    unittest.main()
