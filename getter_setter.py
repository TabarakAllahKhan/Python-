class Person:
    def __init__(self,age):
        self.__age = age
    @property
    def get_age(self):
        return self.__age
    @get_age.setter
    def get_age(self,age):
        self.__age = age


obj=Person(20)
print(obj.get_age)
obj.get_age = 24
print(obj.get_age)
