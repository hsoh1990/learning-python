import unittest


def solution(n):
    return sum(filter(lambda x: n % x == 0, range(1, n//2+1)), n)


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(12), 28)

    def testCase02(self):
        self.assertEqual(solution(5), 6)


if __name__ == '__main__':
    unittest.main()
