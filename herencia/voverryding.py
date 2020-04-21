
clss Employee:
    def setNumberOfWorkingHours(self):
        self.NumberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.NumberOfWorkingHours)


employee = Employee()
employee.setNumberOfWorkingHours()
print("Number Of Working Hours of employee " , end = ' ')
employee.displayNumberOfWorkingHours()
