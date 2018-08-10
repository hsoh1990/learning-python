class Person:
    name = 'default name'

    def __init__(self):
        print('__init__' )

    def print(self):
        print(self.name)

    def __del__(self):
        print('__del__')


p1 = Person()
p1.print()
p1.name = 'wellstone'
p1.print()

