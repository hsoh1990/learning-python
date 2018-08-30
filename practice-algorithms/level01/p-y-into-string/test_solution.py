import unittest


def solution(str):
    return str.lower().count('p') == str.lower().count('y')


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution('pPoooyY'), True)

    def testCase02(self):
        self.assertEqual(solution('Pyy'), False)\


    def testCase03(self):
        self.assertEqual(solution('Ppyy'), True)


if __name__ == '__main__':
    unittest.main()
