class Computer:

    wheels = 4

    def __init__(self):
        print("init")
        self.cpu = 'i5'
        self.ram = 16

    def config(self):
        print(self.cpu,self.ram)

    def compareRam(self, obj2):
        if(self.ram==obj2.ram):
            return True
        else:
            return False

comp1 = Computer()
comp2 = Computer()
print("class wheels: ", Computer.wheels)
print("c1 wheels: ", comp1.wheels)
print("c2 wheels: ", comp2.wheels)
Computer.wheels = 10
comp3 = Computer()
print("c1 wheels: ", comp1.wheels)
print("c2 wheels: ", comp2.wheels)
print("c3 wheels: ", comp3.wheels)

# # comp2.ram = 18
# print(comp1.compareRam(comp2))