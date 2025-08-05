
# name='Tabarak'
#
# for i in name:
#     print(i,end='')
#

# for loop on list

# colors=['red','green','blue','yellow']
#
# for color in colors:
#     print(color)
#     # In the list we can itreate also over indvidual element of lists
#     for i in color:
#         print(i)


# implement do while in python.
# although the do-while loop does not present in python yet we can write code to take work like that
# in do while the first statement will execute must wheater it is true or false ( only for first time)
# in second execution condition will be checked

i=int(input("enter number"))

print(i)  # this is working as a do part of do while loop the first input number will be executed entered by a user

while (i<=38):
    print(i)
    i=i+1
print("done with loop")