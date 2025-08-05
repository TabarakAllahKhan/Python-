# 1) Snake drink water.
# 2) Gun kills snake.
# 3_ Water malfunction gun.

import random
import string

def game(user_choice:str,computer_choice:str):
    if user_choice == computer_choice:
        print("it is draw")
    elif user_choice == "snake" and computer_choice == "water":
        print("you win")
        print(computer_choice)
    elif user_choice == "water" and computer_choice == "snake":
        print("you loose")
        print(computer_choice)
    elif user_choice == "water" and computer_choice == "gun":
        print("you win")
        print(computer_choice)
    elif user_choice == "gun" and computer_choice == "water":
        print("you loose")
        print(computer_choice)
    elif user_choice == "snake" and computer_choice == "gun":
        print("you lost")
        print(computer_choice)
    elif user_choice == "gun" and computer_choice == "snake":
        print("you win")
        print(computer_choice)
    else:
        print("enter valid choice")


user_choice=input('enter your choice bw Snake water and Gun:')
user_choice=user_choice.lower()

options=['snake','water','gun']
computer_choice=random.choice(options)
#print(random.choice(computer_choice))
game(user_choice,computer_choice)
