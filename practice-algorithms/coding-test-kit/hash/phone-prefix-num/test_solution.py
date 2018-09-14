import unittest


def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    strcomp = phone_book.pop(0)

    for ph in phone_book:
        if ph[0:len(strcomp)] == strcomp:
            answer = False
            break

    return answer


class Module1Test(unittest.TestCase):

    def testCase01(self):
        self.assertEqual(solution(['119', '97674223', '1195524421']), False)

    def testCase02(self):
        self.assertEqual(solution(['123', '456', '789'] ), True)

    def testCase03(self):
        self.assertEqual(solution(['12', '123', '1235', '567']), False)


if __name__ == '__main__':
    unittest.main()
