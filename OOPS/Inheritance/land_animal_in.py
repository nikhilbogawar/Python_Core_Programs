# create a class "land_animal" with method "being" & create a class "water_animal" with method "water"
# and create a subclass "frog" that inherits being the classes with method "living" that calls both being and water methods
# Method to Method calling:--------->

class LandAnimal:
    def being(self):
        print("LandAnimal: being the animal")
class WaterAnimal:
    def water(self):
        print("WaterAnimal: water animals")
class Frog(LandAnimal,WaterAnimal):
    def living(self):
        self.being()
        self.water()
        print("Both Water and Land Animal: being the animal also a water animals")
# a1=LandAnimal()
# a2=WaterAnimal()
a3=Frog()
a3.living()
