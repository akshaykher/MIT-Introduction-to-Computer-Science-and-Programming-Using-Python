import datetime

class Person(object):
    def __init__(self,name):
        self.name = name
        self.birthday = None
    def getLastName(self):
        return self.name.split(' ')[-1]
    def Sort(self,other):
        l = []
        l.append(self.getLastName())
        l.append(other.getLastName())
        return l       
    def __str__(self):
        return self.name
    def setBirthday(self,month,day,year):
        self.birthday = datetime.date(year,month,day)
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
p = Person('akshay kher')
p1 = Person('varun sharma')
#l = [p,p1]
#l.sort()
#for i in l: print i
