class Employee:
    comapny='apple'
    def __init__(self,name:str,salary:int):
        self.name = name
        self.salary = salary
    def show(self):
        print(self.name,self.comapny)
    @classmethod
    def change_company(cls,new_company:str):
        cls.company = new_company
    @classmethod
    def changestr(cls,string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e1=Employee('James',1200)
e1.change_company("google")
print(Employee.company)
name="tabarak-2001"
e2=Employee.changestr(name)
print(e2.name)
print(e2.salary)