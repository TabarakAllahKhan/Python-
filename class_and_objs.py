

class Employee:
    emp_id=1
    name="Tabarak"
    age=24
    salary=20000
    def info(self):
        print(f"The id is {self.emp_id} and name is {self.name} and age is {self.age} and salary is {self.salary}")

class Programmer(Employee):
     job_type="python developer"
# obj=Employee()
# b=Employee()

programmer=Programmer()
programmer.age=25
programmer.info()
# b.name="alizai"
#
# b.info()
# obj.info()