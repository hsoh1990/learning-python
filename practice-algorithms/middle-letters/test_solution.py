import unittest


def solution(str):
    return str[(len(str) - 1) // 2:len(str) // 2 + 1]


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution('power'), 'w')

    def testCase02(self):
        self.assertEqual(solution('hsoh'), 'so')


if __name__ == '__main__':
    unittest.main()
