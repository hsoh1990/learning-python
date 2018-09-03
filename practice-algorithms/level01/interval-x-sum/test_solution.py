import unittest


def solution(x, n):
    return [i * x + x for i in range(n)]


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(2, 5), [2, 4, 6, 8, 10])

    def testCase02(self):
        self.assertEqual(solution(4, 3), [4, 8, 12])

    def testCase03(self):
        self.assertEqual(solution(-4, 2), [-4, -8])


if __name__ == '__main__':
    unittest.main()
