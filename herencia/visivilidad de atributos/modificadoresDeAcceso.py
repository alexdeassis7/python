#nomenclatura de scope de la variables
#Public => memberName
#Protected => _memberName   (con un guion bajo)
#Private => __memberName    (con dos guion bajo)

class Car:
    numberOfWheels = 4
    _color = "Black"  #protected
    __yearOfManufacture = 2017   #private no se hereda , internamente python lo almacena asi : _Car__yearOfManufacture

class Bmw(Car):
    def  __init__(self):
        print("Protected attribute color : ", self._color)


car = Car()
print("Car Public attribute numberOfWheels" , car.numberOfWheels)
print("Car  Protected color" , car._color)
#print("private __yearOfManufacture" , car.__yearOfManufacture) esto no se puede
print("private __yearOfManufacture" , car._Car__yearOfManufacture) #esto si se puede, hacerlo solo si es necesario !es mala practica

bmw = Bmw ()
#print("Private attribute __yearOfManufacture : " , car.__yearOfManufacture) no se hereda !
