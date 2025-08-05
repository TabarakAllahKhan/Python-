class Employee:
    company_name="google"
    def __init__(self,name):
        self._name=name
        self.raise_amount=1.0
    def showDetails(self):
        print(f"The name is {self._name} & the raise amount is {self.raise_amount} and the company name is {self.company_name}")


emp1=Employee('Tabarak')
emp1.raise_amount=2.0
emp1.company_name='apple'
emp1.showDetails()
emp2=Employee('Jim')
emp2.raise_amount=3.0
emp2.showDetails()
