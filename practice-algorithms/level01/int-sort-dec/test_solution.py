import unittest


def solution(n):
    answer = sorted(str(n), reverse=True)
    return int(''.join(answer))


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(118372), 873211)

    def testCase02(self):
        self.assertEqual(solution(123), 321)


if __name__ == '__main__':
    unittest.main()
