from functools import reduce


def dbl(n):
    return n*2


my_li=[1,2,3,4,5]

# result=map(dbl,my_li)
# print(list(result))

result1=reduce(lambda x,y:x+y,my_li)

#print(result1)

# filter fun

age=[5,12,17,18,24,32]

adults=filter(lambda x:x>12,age)

print(list(adults))

