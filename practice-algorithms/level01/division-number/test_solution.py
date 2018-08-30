import unittest


def solution(arr, divisor):
    answer = list(filter(lambda num: not num % divisor, sorted(arr)))
    arr = [x for x in arr if not x % divisor]
    print(arr)
    if not answer:
        answer.append(-1)

    return answer


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution([5, 9, 7, 10], 5), [5, 10])

    def testCase02(self):
        self.assertEqual(solution([3, 2, 6], 10), [-1])


if __name__ == '__main__':
    unittest.main()
