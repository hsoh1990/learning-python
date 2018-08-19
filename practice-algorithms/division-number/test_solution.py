import unittest


def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
            answer.sort()
    if answer == []: answer.append(-1)

    return answer


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution([5, 9, 7, 10], 5), [5, 10])

    def testCase02(self):
        self.assertEqual(solution([3, 2, 6], 10), [-1])


if __name__ == '__main__':
    unittest.main()
