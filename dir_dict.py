

my_li=[1,2,3,4]

print(dir(my_li)) # returns all atributes of the object

class Employee:
    def __init__(self,name:str,salary:int):
        self.name = name
        self.salary = salary

obj=Employee("Tabarak",1000)
print(obj.__dict__)