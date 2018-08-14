class Person(object):
    def __init__(self, name, phone_number):
        self.Name = name
        self.PhoneNumber = phone_number

    def PrintInfo(self):
        print('Info(Name: {0}, Phone Number: {1})'.format(self.Name, self.PhoneNumber))

    def PrintPersonData(self):
        print('Person(Name: {0}, Phone Number: {1})'.format(self.Name, self.PhoneNumber))


class Student(Person):
    def __init__(self, name, phone_number, subject, student_id):
        Person.__init__(self, name, phone_number)
        self.Subject = subject
        self.StudentId = student_id

    def PrintInfo(self):
        # print('>> Info(Name: {0}, Phone Number: {1})'.format(self.Name, self.PhoneNumber))
        Person.PrintInfo(self)
        print('>> Info(Subject: {0}, Student Id: {1})'.format(self.Subject, self.StudentId))


P = Person('hsoh', '010-0000-0000')
S = Student('student', '010-0000-0000', 'program', '010')

print(P.__dict__)
print(S.__dict__)
print(S.PrintInfo())
print(issubclass(Student, Person))
print(Student.__bases__)

