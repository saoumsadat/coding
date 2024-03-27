class Library:
    def __init__(self, location, catDict):
        self.name = location
        self.categoryDict = catDict
        self.borrowerDict = {}
    
    def details(self):
        print(f"{self.name} Library details")
        print(f"Borrower details:\n{self.borrowerDict}")
        print(f"Books availability:\n{self.categoryDict}")

class Reader:
    def __init__(self, name):
        self.name = name
        self.bookCount = 0
        self.categoryDict = {}
    
    def borrow(self, lib, *catList):
        for bookCat in catList:
            if self.bookCount >= 5:
                print("You cannot borrow more than 5 books.")

            elif bookCat not in lib.categoryDict.keys():  #category not in the library
                print("Category is not in the library.")

            elif lib.categoryDict[bookCat] == 0:    #remaining book count is 0
                print(f"{bookCat} books are not available at the moment.")

            else:   #available

                #changing library info
                lib.categoryDict[bookCat] -= 1  
                if self.name in lib.borrowerDict.keys():    #borrowed before
                    lib.borrowerDict[self.name] += 1
                else:   #first time borrow
                    lib.borrowerDict[self.name] = 1

                #changing reader info
                self.bookCount += 1
                if bookCat in self.categoryDict.keys():     #category already borrowed before
                    self.categoryDict[bookCat] += 1
                else:   #category never borrowed before
                    self.categoryDict[bookCat] = 1
                
                print(f"{bookCat} book is borrowed successfully.")
                
    def readerInfo(self, catArg = None):
        if not(catArg):    #no arg passed
            print(f"{self.name}, you have {self.bookCount} book(s) with you.")
            for category in self.categoryDict.keys():
                print(f"Books on {category}: {self.categoryDict[category]}")
        
        else:    #arg passed
            print(f"{self.name}, you have {self.categoryDict[catArg]} {catArg} book(s) with you.")



L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()
