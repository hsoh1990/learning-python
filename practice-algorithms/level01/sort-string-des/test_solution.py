import unittest


def solution(strings):
    return ''.join(sorted(strings, reverse=True))


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution('Zbcdefg'), 'gfedcbZ')


if __name__ == '__main__':
    unittest.main()
