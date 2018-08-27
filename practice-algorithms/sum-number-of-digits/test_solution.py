import unittest


def solution(n):
    return sum([int(item) for item in str(n)])


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(123), 6)

    def testCase02(self):
        self.assertEqual(solution(987), 24)


if __name__ == '__main__':
    unittest.main()