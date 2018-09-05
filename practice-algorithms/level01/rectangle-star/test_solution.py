import unittest


def solution(str):
    a, b = map(int, str.split(' '))
    print(a, b)
    return ('*' * a + '\n') * b


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution('5 3'), '*****\n*****\n*****')


if __name__ == '__main__':
    unittest.main()
