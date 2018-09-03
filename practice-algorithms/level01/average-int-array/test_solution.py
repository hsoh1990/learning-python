import unittest


def solution(arr):
    return sum(arr)/len(arr)


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution([1, 2, 3, 4]), 2.5)

    def testCase02(self):
        self.assertEqual(solution([5, 5]), 5)


if __name__ == '__main__':
    unittest.main()
