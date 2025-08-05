import numbers


def calculatearea(length,width):
    pass
    # area=length*width
    # return area
    # # pass keyword-> Null operation
    # it will run the code even if it is empty it basically create a placeholder for
    # future code.

# length=9
# width=8
#
# total_area=calculatearea(length, width)
#
# print(total_area)

# getting numbers as tuples

def average(*numbers):   # if you dont sure number of arguments you can use * symbol
                         # this will return tuple of arguments
    print(type(numbers))
    sum=0
    for i in numbers:
       sum=sum+i
    print(sum/len(numbers))


average(1,4,9)

