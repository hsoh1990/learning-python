import unittest


def solution(strings, n):
    answer = sorted(strings)
    answer = sorted(answer, key=lambda answer: answer[n])
    return answer


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution(['sun', 'bed', 'car'], 1), ['car', 'bed', 'sun'])

    def testCase02(self):
        self.assertEqual(solution(['abce', 'abcd', 'cdx'], 2), ['abcd', 'abce', 'cdx'])


if __name__ == '__main__':
    unittest.main()
