import unittest


def solution(dartResult):
    answer = 0
    preNum = 0
    curNum = 0
    # S=*1 / D=*2 / T=*3
    # * = 지금점수 *2 전점수 *2
    # # = 지금점수 -

    return answer


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution('1S2D*3T'), 37)

    def testCase02(self):
        self.assertEqual(solution('1D2S#10S'), 9)

    def testCase03(self):
        self.assertEqual(solution('1D2S0T'), 3)

    def testCase04(self):
        self.assertEqual(solution('1S*2T*3S'), 23)

    def testCase05(self):
        self.assertEqual(solution('1D#2S*3S'), 5)

    def testCase06(self):
        self.assertEqual(solution('1T2D3D#'), -4)

    def testCase07(self):
        self.assertEqual(solution('1D2S3T*'), 59)


if __name__ == '__main__':
    unittest.main()
