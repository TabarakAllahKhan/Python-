

# class Employee():
#     def __init__(self):
#         self.__name="Tabarak" # private variable
#         self._age=100 # protected variable
#
#
# a=Employee()
# #print(a.__name)
# print(a._Employee__name)
# print(a._age)

class Library:
    def __init__(self,no_of_books:int,books:list):
        self.no_of_books=no_of_books
        self.books=books
    def check(self):
        if self.no_of_books != len(self.books):
            print("An error")
        
        else:
            print("The no of books and len of books are equal")
    def info(self):
        print(f"The no of books in library is : {self.no_of_books} and the books are: {self.books}")


book=Library(2,["Biology","Intro to Computer Science","History of islam"])
book.check()
book.info()

