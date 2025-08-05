class Parent:
    def __init__(self,name,id):
        self._name=name
        self._id=id

class Child(Parent):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

x=Child("John",1,"python")
print(x._name)
print(x._id)
print(x.lang)