
#
# ep1={
#     130:90,
#     120:34,
#     233:100,
#     100:90
# }
#
# ep2={
#     122:23,
#     124:24,
#     300:20,
#     190:4
# }
#
# ep1.update(ep2)
#
#
# print(ep1)

thisdict = {
   "brand": "Ford",
   "model": "Mustang",
   "year": 1964
 }

#thisdict.pop("brand") removes the dictonary key along with value

#thisdict.popitem()
#print(thisdict)  # removes last item from the dictionary

#thisdict.clear() # returns empty list
#print(thisdict)

#for i in thisdict:
    #print(i)  # this will return the key of dictonary

# for i in thisdict:
#     print(thisdict[i]) # this will return the value of the list

# for i in thisdict.values():
#  print(i)   # another way to print values

mydict = thisdict.copy()
print(f"The copy of this dictionary is {mydict}")

# nested dictonary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])