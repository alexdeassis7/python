
definimos una clase 

class Employee:
	name = "alex"
	designation = "Sales Executive"
	salesMadeThisWeek = 6
	def hasAchievedTarget(self):
		if self.salesMadeThisWeek >= 5:
			print("Target has ben")
		else:
			print("Target has not ben")

			instanciamos un objeto 
>>> employedOne = Employee()
>>> 
accedo a un atributo 
>>> employedOne.name
'alex'
>>> employedOne.designation
'Sales Executive'


accedo a un metodo
>>> employedOne.hasAchievedTarget
<bound method Employee.hasAchievedTarget of <__main__.Employee object at 0x00000211AFC9E730>>
>>> employedOne.hasAchievedTarget()
Target has ben
>>> employedDos

		TODO EN PYTHON ES UN OBJETO!!
>>> numbers = [1 , 2 , 5 ]
>>> type(numbers)
<class 'list'>
>>> numbers.append(7)
>>> numbers
[1, 2, 5, 7]