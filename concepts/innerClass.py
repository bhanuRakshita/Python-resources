class Student:
    def __init__(self, name, rollno, brand, ram):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop(brand,ram)

    def show(self):
        print(self.name,self.rollno, self.lap.brand, self.lap.ram)
    
    class Laptop:
        def __init__(self, brand, ram) -> None:
            self.brand = brand
            self.ram = ram

stu1 = Student("Bhanzz",143428217,"Lenovo","i8")

stu1.show()