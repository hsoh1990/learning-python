import unittest


def solution(phone_number):
    return str(phone_number[-4:]).rjust(len(phone_number), '*')


class Module1Test(unittest.TestCase):
        def testCase01(self):
            self.assertEqual(solution('01033334444'), '*******4444')

        def testCase02(self):
            self.assertEqual(solution('027778888'), '*****8888')


if __name__ == '__main__':
    unittest.main()