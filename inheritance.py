# single level inheritance

class Animal(object):
    def __init__(self,name,specie):
        self.name=name
        self.specie=specie
    def make_sound(self):
        print("Animal make sound")
    def info(self):
        print(f"name is {self.name} ,specie is {self.specie} ")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,specie="german shepred")
        self.breed=breed

    def make_sound(self):
        print("Dog make sound")
    def info(self):
        print(f"name is {self.name} ,specie is {self.breed} ")

dog=Dog("tommy","hisky")

dog.info()
dog.make_sound()