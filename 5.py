class A:
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input("Enter a string")
    def printString(self):
        print(self.s.upper())
obj=A()
obj.getString()
obj.printString()
