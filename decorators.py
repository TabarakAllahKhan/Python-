

# A decorator is a function that takes another function as argument
# and return a new function that modifies the behaviour of orignal function
def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("Thanks for using me")
    return mfx

@greet
def hello():
    print("hello")




greet(hello)
hello()


# read args and kwargs