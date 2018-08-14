from NegativeDivisionError import NegativeDivisionError


def PositiveDivide(a, b):
    if b < 0:
        raise NegativeDivisionError(b)
    return a / b

def foo(x):
    assert type(x) == int, 'Input value must be integer'
    return x * 10


if __name__ == '__main__':
    try:
        ret = PositiveDivide(10, -3)
        print('10 / -3 = {0}'.format(ret))
    except NegativeDivisionError as e:
        print('error - NegativeDivisionError is ', e.value)
    except ZeroDivisionError as e:
        print('error - ZeroDivisionError is ', e.args[0])
    except Exception as e:
        print(e.args)

    ret = foo('x')
    print(ret)
