


# Parent Class Animals

class Animals:
    species = "unknown"
    habitat = "unknown"
    diet = "unknown"
    arms = 0
    legs = 0


    def Info(self):
        msg = "\nSpecies: {}\nHabitat: {}\nDiet: {}\nArms: {}\nLegs: {}".format(self.species, self.habitat, self.diet, self.arms, self.legs)
        return msg


# Child class Reptiles

class Reptiles(Animals):
    species = "Russian Tortoise"
    habitat = "Burrow"
    diet = "Herbivore"
    life_span = "50-100 years"
    sleep_pattern = "Hibernation"

    def Info(self):
        msg = "\nSpecies: {}\nHabitat: {}\nDiet: {}\nLifespan: {}\nSleep pattern: {}\nArms: {}\nLegs: {}".format(self.species, self.habitat, self.diet, self.life_span, self.sleep_pattern, self.arms, self.legs)
        return msg


# Child class Birds

class Birds(Animals):
    species = "Saker Falcon"
    habitat = "Eastern Europe"
    diet = "Carnivore"
    legs = 2
    airspeed = "Up to 200mph"
    wingspan = "105-129cm"

    def Stoop(self):
        print("Flying upwards to a high altitude, they then dive-bomb back down at breathtaking speeds to catch their prey!")


#Invokes the methods inside each class for Reptiles & Birds


tortoise = Reptiles()
tortoise.Info()

falcon = Birds()
falcon.Stoop()

    
