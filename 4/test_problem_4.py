import unittest
import problem_4

class Test4(unittest.TestCase):

    def test_palindrome_checker(self):
        n = problem_4.Problem_4()
        self.assertEqual(n.is_pal(9009), True)



if __name__ == '__main__':
    unittest.main()