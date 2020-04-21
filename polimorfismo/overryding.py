class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

#clase que hereda de Employee
class Trainee(Employee):
    #aca estamos haciendo override del padre pisando las horas de trabajo por 45
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45
#con super invocamos a cualquier metod de la clase padre
    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
#end es para agregar unos espacios
print("Number Of Working Hours of employee " , end = '    ')
employee.displayNumberOfWorkingHours()

trainee = Trainee()
#imprimimos resultados polimorficos
trainee.setNumberOfWorkingHours()
print("Number Of Working Hours of Trainee " , end = '    ')
trainee.displayNumberOfWorkingHours()

#usamos funcion que hace reset de horas
trainee.resetNumberOfWorkingHours()
print("RESET Number Of Working Hours of Trainee " , end = '    ')
trainee.displayNumberOfWorkingHours()
