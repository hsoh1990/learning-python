import unittest


def solution(participant, completion):
    for co in completion:
        participant.remove(co)
    print(participant)
    return participant[0]


class Module1Test(unittest.TestCase):

    def testCase01(self):
        self.assertEqual(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']), 'leo')

    def testCase02(self):
        self.assertEqual(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']), 'vinko')

    def testCase03(self):
        self.assertEqual(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']), 'mislav')


if __name__ == '__main__':
    unittest.main()
