class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return "Vector({0},{1},{2})".format(self.x,self.y,self.z)
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

v=Vector(1,2,3)
print(v)
v2=Vector(4,5,6)
print(v+v2)