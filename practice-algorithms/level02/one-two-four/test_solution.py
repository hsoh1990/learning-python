import unittest


def solution(n):
    answer = ''
    nums = ['1', '2', '4']
    quotient = -1

    while quotient != 0:
        quotient = int((n - 1) / 3)
        remainder = (n - 1) % 3
        answer = nums[remainder] + answer
        n = quotient
    return int(answer)


class Module1Test(unittest.TestCase):

    def testCase01(self):
        self.assertEqual(solution(1), 1)

    def testCase02(self):
        self.assertEqual(solution(2), 2)

    def testCase03(self):
        self.assertEqual(solution(3), 4)

    def testCase04(self):
        self.assertEqual(solution(4), 11)

    def testCase10(self):
        self.assertEqual(solution(10), 41)


if __name__ == '__main__':
    unittest.main()
