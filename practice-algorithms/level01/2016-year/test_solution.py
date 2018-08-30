import unittest


def solution(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(5, 24), 'TUE')

    def testCase02(self):
        self.assertEqual(solution(12, 31), 'SAT')


if __name__ == '__main__':
    unittest.main()
