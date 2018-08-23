import unittest


def solution(n):
    answer = '수박' * (n // 2 + 1)
    return answer[:n]


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(3), '수박수')

    def testCase02(self):
        self.assertEqual(solution(4), '수박수박')


if __name__ == '__main__':
    unittest.main()
