

class Calculate:
    def __init__(self,num):
        self._num=num
    def addtonum(self,n):
        self._num+=self._num+n
    @staticmethod
    def calculate(num1,num2):
        return num1+num2

a=Calculate(5)
print(a.calculate(1,2))