#
#
# def myfun(n):
#     return lambda a:n*a
#
#
# const=myfun(5)
#
# print(const(10))

user_input = input("Enter a number between 5 and 9 (or type 'quit' to exit): ")

if user_input.lower() == 'quit':
    raise NameError("The user quits")
else:
    try:
        a = int(user_input)
        if a < 5 or a > 9:
            raise ValueError("Invalid Number or input")
    except ValueError:
        raise ValueError("Invalid input: please enter a number between 5 and 9 or type 'quit'")
