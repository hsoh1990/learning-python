import unittest


def solution(seoul):
    return '김서방은 {0}에 있다'.format(seoul.index('Kim'))


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(['Jane', 'Kim']), '김서방은 1에 있다')

    def testCase02(self):
        self.assertEqual(solution(['Jane', 'Kim', 'oh', 'back']), '김서방은 1에 있다')


if __name__ == '__main__':
    unittest.main()
