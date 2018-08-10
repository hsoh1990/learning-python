value = int(input('input value: '))

if value < 5:
    print('value:' + str(value) + ' < 5')
elif 5 < value < 10:
    print('5 < ' + str(value) + ' < 10')
else:
    print('10 =< ' + str(value))
