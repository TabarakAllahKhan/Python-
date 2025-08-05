mytuple = (1, 2, 3, 4, 5,5)

# print(tuple[:-3])
#
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","apple")
# print(fruits[2:5])

# Operations on Tuple

# Adding Item to Tuple
# As we cant change tuple we have to convert it in list first then agin in tuple

# convert=list(mytuple)
# convert.pop(2)
# print(convert)
# convert.append(20)
#
# mytuple=tuple(convert)
# print(mytuple)

# However we can concatinate 2 tuples to create a third new tuple

# new_tuple=mytuple + fruits
#
# print(new_tuple)

# Count the occurance of items

res=mytuple.index(5,2,6)
print(res)
