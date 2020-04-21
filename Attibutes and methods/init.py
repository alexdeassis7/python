class Employee:
    #init se llama cuando se crea el objeto 
    def __init__(self , name):
        self.name=name
        
    def enterEmployeeDetails(self):
        self.name="alex"
    
    def displayEmployeeDetails(self):
        print(self.name)
        
employed = Employee("alex")
employedTwo = Employee("jose")

employed.displayEmployeeDetails() 

employedTwo.displayEmployeeDetails()        