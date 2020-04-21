 #static method
 
 #intanse method
 
class Empleado:
    def detalleDeEmpleado(self):#metodo de intancia
        self.nombre = "pedro"
    
    @staticmethod    
    def mensajeBienvenida():
        print("soy estatico welcome to Cognizant!!!")
        
e1 = Empleado()

e1.detalleDeEmpleado()

print("metodo de instancia " +e1.nombre)

e1.mensajeBienvenida()