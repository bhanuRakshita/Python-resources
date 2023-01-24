class Student:
    school = "Seneca"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    #instance method
    def avg(self):
        print ((self.m1+self.m2+self.m3)/3)
    
    #class method
    @classmethod
    def getSchool(cls):
        print (cls.school)

    #static method
    @staticmethod
    def info():
        print("this isssssss student class")

stu1 = Student(43,78,90)
stu1.avg()
Student.getSchool()
stu1.info()