import unittest


def solution(x):
    return not x % sum([int(el) for el in str(x)])


class Module1Test(unittest.TestCase):

    def testCase01(self):
        self.assertEqual(solution(10), True)

    def testCase02(self):
        self.assertEqual(solution(12), True)

    def testCase03(self):
        self.assertEqual(solution(11), False)

    def testCase04(self):
        self.assertEqual(solution(13), False)


if __name__ == '__main__':
    unittest.main()
