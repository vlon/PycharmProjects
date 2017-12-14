# coding = utf-8

class SchoolMember:
    '''代表学校里的成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:"{}" Age:"{}".'.format(self.name, self.age), end=' ')

class Teacher(SchoolMember):
    '''代表一位老师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))



t = Teacher('Mrs. Tang', 40, 3000)
s = Student('An', 25, 75)

print()

menbers = [t, s]
for menber in menbers:
    menber.tell()
