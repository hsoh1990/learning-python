import unittest


def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(3, 5), 12)

    def testCase02(self):
        self.assertEqual(solution(3, 3), 3)

    def testCase03(self):
        self.assertEqual(solution(5, 3), 12)


if __name__ == '__main__':
    unittest.main()
