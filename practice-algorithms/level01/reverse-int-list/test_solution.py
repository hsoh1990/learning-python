import unittest


def solution(n):
    return list(reversed([int(item) for item in str(n)]))


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(12345), [5, 4, 3, 2, 1])

    def testCase02(self):
        self.assertEqual(solution(0), [0])

    def testCase02(self):
        self.assertEqual(solution(123123), [3, 2, 1, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
