
class Person:
   species="human"
   def __init__(self,name,occ):
        self.name=name
        self.occ=occ
   def info(self):
     print(f"Name is :{self.name}, Occ is :{self.occ},species is :{self.species}")
Person.species="alien"
a=Person("Tabarak","Ai engineer")
b=Person("Essa","Ecommerce Expert")

a.info()
b.info()
