import unittest


def solution(s):
    opened = 0
    for el in s:
        # if el == '(':
        #     opened += 1
        # elif el == ')':
        #     opened -= 1
        opened = opened + 1 if el == '(' else opened - 1
        if opened < 0:
            break
    return opened == 0


class Module1Test(unittest.TestCase):

    def testCase01(self):
        self.assertEqual(solution('()()'), True)

    def testCase02(self):
        self.assertEqual(solution('(())()'), True)

    def testCase03(self):
        self.assertEqual(solution(')()('), False)

    def testCase04(self):
        self.assertEqual(solution('(()('), False)


if __name__ == '__main__':
    unittest.main()
