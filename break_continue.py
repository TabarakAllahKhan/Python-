

#Question:
#Write a Python program that prints numbers from 1 to 10, but stops the loop when it reaches the number 6.

# for i in range(1,10,1):
#     print(i)
#     if(i==5):
#          break

#Question:
# a Python program that prints all odd numbers between 1 and 20, skipping any number that is divisible by 5.

# for i in range(1,20,1):
#     if(i%5==0):
#         continue
#     if(i%2!=0):
#         print(i)

# total=0
# while True:
#     number = int(input("Enter a number:"))
#     if number < 0:
#         continue
#     if number == 0:      # This code is also the emulation of do-while loop
#         break
#     total+=number
#
#
# print('The sum of numbers is:',total)

# Another code example

i=0

while True:
    print(i)
    i=i+1
    if (i==20):
        break


