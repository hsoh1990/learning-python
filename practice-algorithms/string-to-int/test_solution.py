import unittest


def solution(s):
    return int(s)


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution("1234"), 1234)

    def testCase02(self):
        self.assertEqual(solution('-1234'), -1234)


if __name__ == '__main__':
    unittest.main()
