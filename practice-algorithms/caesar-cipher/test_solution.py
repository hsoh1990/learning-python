import unittest


def solution(s, n):
    li = [ord(x) for x in s]
    answer = []
    for el in li:
        tmp = el + n
        if 96 < el < 123 and tmp > 122:
            tmp = 97 + n - (122 - el + 1)
        if 64 < el < 91 and tmp > 90:
            tmp = 65 + n - (90 - el + 1)
        if el == 32:
            answer.append(" ")
        else :
            answer.append(chr(tmp))
    return ''.join(answer)


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution('AB', 1), 'BC')

    def testCase02(self):
        self.assertEqual(solution('z', 1), 'a')

    def testCase03(self):
        self.assertEqual(solution('a B z', 4), 'e F d')


if __name__ == '__main__':
    unittest.main()
