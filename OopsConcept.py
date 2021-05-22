#Class is user defined blue print or prototype
# It have methods (when function used inside class), constructor, class/instance variables etc


class Calculator:

    num = 100  #class variables

    # constructor name should be __init__
    # Self is object reference who is calling
    def __init__(self, a, b):
        print("when object created default constructor called automatically")
        self.firstNumber = a #Instance variable
        self.secondNumber = b

    def getdata(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num  #called class variable


obj = Calculator(2, 3)
obj.getdata()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.getdata()
print(obj1.summation())

