import unittest
from math import sqrt


def solution(n):
    return -1 if sqrt(n) % 1 else (sqrt(n)+1) **2


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(121), 144)

    def testCase02(self):
        self.assertEqual(solution(3), -1)


if __name__ == '__main__':
    unittest.main()


