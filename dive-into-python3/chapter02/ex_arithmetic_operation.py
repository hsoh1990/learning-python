import fractions
import math


def is_it_true(anything):  # 1
    if anything:
        print("yes, it's true")
    else:
        print("no, it's false")


if __name__ == '__main__'"":
    # 나누기
    print(11 / 2)
    print(11 // 2)
    print(-11 // 2)
    print(11.0 // 2)

    # 제곱
    print(11 ** 2)

    # 분수
    x = fractions.Fraction(1, 3)
    print(x)
    print(fractions.Fraction(6, 4))

    # 수학관련
    print(math.sin(math.pi / 2))

    # boolean context 에서 숫자는 0만 거짓
    is_it_true(1)
    is_it_true(-1)
    is_it_true(0)
