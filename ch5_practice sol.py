
# dict_translation={
#     "Kia Hal Hain":"Hello",
#     "Kia kar rehe ho":"What are you doing?",
#     "Tumhara nam kia h":"What's your name?"
# }
#
# for x,y in dict_translation.items():
#     print(x,y)


# numbers=set()
#
# for x in range(0,9):
#     user=int(input(f"Enter a {x} number:"))
#     numbers.add(user)
#
# print(f"The unique numbers is: {numbers}")


# myset={1,2,8,"8"}
# print(myset)

# myset=set()
#
# myset.add(20)
# myset.add(20.0)
# myset.add("20")
# print(myset)
# print(len(myset))


# friends_dict={}
#
# for i in range(0,3):
#      name=input(f"User {i} your name: ")
#      favt_lang=input(f"User {i} your favorite language: ")
#      friends_dict[name]=favt_lang
#
# print(friends_dict)

# s={9,4,5,"tabarak",[1,2]} #     this will raise error bcz the set can contain only that
#                           #     elements that are immutable but list is mutable means it
#                           # can be changed so it can't be the element of a set
# print(s)
# s={9,4,5,"tabarak",(1,2)}
# print(s)

grades = {
    ("Ali", "Math"): 85,
    ("Ali", "Science"): 78,
    ("Zara", "Math"): 92
}

print(grades[("Ali", "Math")])# Output: 85

for (name,subject),marks in grades.items():
    print(f"{name}-{subject}:{marks}")


