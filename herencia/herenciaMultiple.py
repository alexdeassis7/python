class OperatingSystem:
	multitasking = True
	name = "Mac OS"

class Apple:
	website = "www.apple.com"
	name = "Apple"

#esta clase es hija de dos padres
class MacBook(OperatingSystem , Apple):#el orden de la herencia si importa
	def __init__(self):
		if self.multitasking is True:
			print("This is a multi tasking system . Visis {} for more details ".format(self.website))
#por estar en ambos padres el atributo toma siempre el atributo de la clase que pongo a la izquierda en la herecia (OperatingSystem en este caso)
			print("Name  :" ,self.name)
mac = MacBook()
