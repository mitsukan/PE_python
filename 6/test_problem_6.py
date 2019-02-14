import unittest
import problem_6

class Test6(unittest.TestCase):

    def test_can_work_out_example(self):
        self.assertEqual(problem_6.sum_of_squares(10), 385)




if __name__ == '__main__':
    unittest.main()