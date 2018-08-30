import unittest


def solution(s):
    answer = ''
    li = s.split(' ')
    for el in li:
        for i in range(len(el)):
            if i % 2 == 0:
                answer += el[i].upper()
            else:
                answer += el[i].lower()
        answer += ' '
    answer = answer[:-1]
    return answer


def solution2(s):
    answer = ' '.join(
        map(
            lambda word: ''.join([alpha.lower() if i % 2 else alpha.upper() for i, alpha in enumerate(word)]),
            s.split(' ')
        )
    )
    return answer


class Module1Test(unittest.TestCase):
    def testCase01(self):
        self.assertEqual(solution('try hello world'), 'TrY HeLlO WoRlD')

    def testCase02(self):
        self.assertEqual(solution2('try hello world'), 'TrY HeLlO WoRlD')


if __name__ == '__main__':
    unittest.main()
