import unittest


def solution(n, m):
    gcd = lambda a, b: a if b == 0 else gcd(b, (a % b))
    lcm = lambda a, b: a * b / gcd(a, b)
    return [gcd(n, m), lcm(n, m)]


class Module1Test(unittest.TestCase):

    def testCase01(self):
        self.assertEqual(solution(3, 12), [3, 12])

    def testCase01(self):
        self.assertEqual(solution(2, 5), [1, 10])


if __name__ == '__main__':
    unittest.main()
