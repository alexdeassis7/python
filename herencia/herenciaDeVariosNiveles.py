class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = "Tonewood"

class Guitar(StringInstruments):
       def __init__(self):
            self.numberOfStrings = 6
            print("This guitar consits of {} strings . It is nade of {} and it can play {} Keys ".format(self.numberOfStrings, self.typeOfWood, self.numberOfMajorKeys))


guitar = Guitar()
