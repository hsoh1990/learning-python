import unittest


def solution(num):
    return "Odd" if num % 2 else "Even"


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(3), "Odd")

    def testCase02(self):
        self.assertEqual(solution(4), "Even")


if __name__ == '__main__':
    unittest.main()
