class vsCode:
    def execute(self):
        print("vscode compiling and running")

class myIDE:
    def execute(self):
        print("my IDE compiling and running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = myIDE()
lap1 = Laptop()
lap1.code(ide)
