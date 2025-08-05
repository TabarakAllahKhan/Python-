
# Reading A File
# f=open("file.txt","rb")
# text=f.read()
# print(text)
# f.close()


# Writing A file

# f=open("file.txt","a")
# text=f.write("And I have studied from kfueit")
# print(text)
# f.close()

# with statement

# try:
#   with open("file.txt","w") as f:
#       lines=['first\n','second\n','third']
#       f.writelines(lines)
# except Exception as e:
#     print(e)

# Seek fun()

# with open("file.txt",'r') as f:
#     f.seek(10)
#     print(f.tell())  # The tell function gives the current pointer position in a file
#     data=f.read(5)
#     print(data)

#The seek() method lets you move that pointer to any position you want.


# Truncate funtion

# with open("sample.txt","w") as f:
#     f.writelines("hello World")
#     f.truncate(5) # write the 5 five characters of file
#
# with open("sample.txt","r") as f:
#     print(f.read())



