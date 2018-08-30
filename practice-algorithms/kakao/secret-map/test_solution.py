import unittest


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(str(bin(arr1[i] | arr2[i]))[2:].rjust(n, ' ').replace('1', '#').replace('0', ' '))
    return answer


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(
            solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]),
            ["#####","# # #", "### #", "#  ##", "#####"])

    def testCase02(self):
        self.assertEqual(
            solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]),
            ["######", "###  #", "##  ##", " #### ", " #####", "### # "])


if __name__ == '__main__':
    unittest.main()
