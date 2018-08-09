def is_it_true(anything):
    if anything:
        print("yes, it's true")
    else:
        print("no, it's false")


if __name__ == '__main__':
    a_tuple = ("a", "b", "mpilgrim", "z", "example")
    print(a_tuple)
    print(a_tuple[0])
    print(a_tuple[-1])
    print(a_tuple[1:3])

    # tuple 변경 불가능
    # a_tuple.append("new")
    # a_tuple.remove("z")

    print(a_tuple.index("example"))
    print("z" in a_tuple)
    print('--------------------------------------')
    # tuple로 참거짓 판단
    is_it_true(())
    is_it_true(('a', 'b'))
    is_it_true((False,))
    print(type((False)))
    print(type((False,)))
    print('--------------------------------------')
    # tuple로 여러 값을 한번에 할당
    v = ('a', 2, True)
    (x, y, z) = v
    print(x)
    print(y)
    print(z)
    (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
    print(MONDAY)
