import unittest


def solution(num):
    answer = 0
    collatzFunc = lambda n: int(n / 2) if not n % 2 else n * 3 + 1
    while num != 1:
        num = collatzFunc(num)
        answer += 1
        if answer == 100:
            answer = -1
            break
    return answer


class Module1Test(unittest.TestCase):

    def testCase01(self):
        self.assertEqual(solution(6), 8)

    def testCase02(self):
        self.assertEqual(solution(16), 4)

    def testCase03(self):
        self.assertEqual(solution(626332), -1)


if __name__ == '__main__':
    unittest.main()
