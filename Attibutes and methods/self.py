print("inicio")
class Employee:
    def employedDetails(self):    
        self.name = "ramon" #atributo de instancia 
        age = 30 # age es de sope de method 
        print("Age :" , age)

    def printEmployeeDetails(self):
        print("imprimo desde otro metodo")
        print("Name: " ,self.name)
        #print("Age : " , age) esto no se puede por que age es un parametro del otro metodo 
        
        
        
        
e1 = Employee()
#modo 1 call method *esta es la sintaxis abreviada de invocacion a un metodo 
e1.employedDetails()
#mode 2 call method . esto es lo que realiza internamente el interprete cuando invocamos a un metodo
Employee.employedDetails(e1)
print(e1.name)

#uso la funcion 2
e1.printEmployeeDetails()

print("end culo")