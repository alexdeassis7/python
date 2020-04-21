class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    
	def displayAvailableBooks(self):
        print()
        print("Available Books")
        for book in self.availableBooks:
            print (book)            
		pass
		
	def lendBook(self):
		pass
	
	def addBook(self):
		pass
	
class Customer:
	def requestBook(self):
        print("ingrese el nombre del libro que quiere llevar: ")
        self.book = input()
        return self.book
   
		pass
		
	def returnBook(self):
		pass
        
library = Library('libro uno' , 'libro dos' , 'libro 3 ');
