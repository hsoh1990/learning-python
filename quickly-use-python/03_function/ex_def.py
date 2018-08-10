def Times(a, b):
    return a * b


print(Times)
print(Times(10, 10))
defTimes = Times
print(defTimes)
valTimes = Times(10, 10)
print(valTimes)


def swap(x, y):
    return y, x


print(swap(1, 2))
a, b = swap(1, 2)
print('a =', a, 'b =', b)


def change(c):
    c[0] = 'H'


wordlist = ['J', 'A', 'M']
change(wordlist)
print(wordlist)






