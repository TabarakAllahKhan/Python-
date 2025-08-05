import os


# folders=os.listdir('Python ChapterWise Notes')
#
# print(folders)

print(os.getcwd())

x=5

def justFun():
    global x
    x=4
    return x

print(x)
print(justFun())
print(x)
