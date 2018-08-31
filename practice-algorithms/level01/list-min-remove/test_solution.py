import unittest


def solution(arr):
    # arr.remove(min(arr))
    # if len(arr) == 0:
    #     arr.append(-1)
    # return arr

    return [i for i in arr if i > min(arr)]


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution([4, 3, 2, 1]), [4, 3, 2])

    def testCase02(self):
        self.assertEqual(solution([10]), [-1])


if __name__ == '__main__':
    unittest.main()
