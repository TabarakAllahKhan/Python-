from unittest import case

# Match Case Statement are the Switch cases (Like in java,c++ or any language has switch case statements) of Python
# Important Note unlike c++ or other languages we have to use break to break out of the switch if case matches but
#in python it is not necessary to use break in the match case statement
x=6

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")

    case _:   # default case only execute if above of all cases does not execute
        print("x is less than 10")

