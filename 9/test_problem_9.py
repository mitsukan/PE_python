import unittest
import problem_9

class Test9(unittest.TestCase):

    def test_get_root(self):
        self.assertEqual(problem_9.get_root(9), 3)



if __name__ == '__main__':
    unittest.main()