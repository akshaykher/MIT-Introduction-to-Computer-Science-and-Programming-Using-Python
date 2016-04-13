class Student(object):
    foo = 3
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.gender = c
    def __str__(self):
        return "<"+self.name+","+str(self.age)+","+self.gender+">"
        

student1 = Student('akshay',24,'M')
student2 = Student('rahul',25,'M')
student3 = Student('Manvi',23,'F')

#print isinstance(student1,Student)