def Times(a=10, b=10):
    return a * b


print(Times())
print(Times(5))
print(Times(b=4))


def test(*args):
    print(args)
    res = []
    for arg in args:
        res.append(arg)
    return res


print(test(1, 2, 3))
