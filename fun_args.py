
# There are 4 types of arguments
# 1) Default Argument
# 2) Required Argument
# 3) Variable Length Argument
# 4) Keyword Argument

# Exmpale of Require Argument
# def avg(a:int,b:int):
#     print(f"avg is {(a+b)/2}")
#
#
# avg(10,20)

# Example of Default Argument

#Default Arguments is a parameter that have a predefined value if no value is passed during the function call. This following example illustrates Default arguments to write functions in Python.
# def area(length:int,width=14):
#     area_of = length*width
#     print(area_of)
#
# area(width=10,length=5)

# variable length args


# def avg(*numbers:int):
#     sum=0
#     for i in numbers:
#         sum+=i
#     print("The avg is  ", sum/len(numbers))
#     print(type(numbers))
#
# avg(1,2,3,4,5)

def name(**name):
    print(type(name))
    print("Hello",name['faname'],name['mname'],name['lname'])


name(mname="Allah",faname='Tabarak',lname='Khan')