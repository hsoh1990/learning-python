value = 3
while value > 0:
    print(value)
    value -= 1

li = ['apple', 100, 1.11]
for l in li:
    print(l)

iterator = iter(li)
for it in iterator:
    print(it)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 10, 1)))
print(list(range(10, 0, -1)))
print(list(range(10, 20, 2)))

for i in L:
    if i > 5:
        break
    print('for, break: {0}'.format(i))

for i in L:
    if i % 2 == 0:
        continue
    print('for, continue: {0}'.format(i))

for i in range(len(L)):
    print('index: {0}, value: {1}'.format(i, L[i]))
for i in enumerate(L):
    print(i)
