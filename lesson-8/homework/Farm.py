class Animal:
   
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
   
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Cow(Animal):

    def __init__(self, name, age, weight, milk_production):
        super().__init__(name, age, weight)
        self.milk_production = milk_production

    def make_sound(self):
        return "Moo"

    def produce_milk(self):
        return f"{self.name} produces {self.milk_production} liters of milk"

class Chicken(Animal):
    
    def __init__(self, name, age, weight, egg_count):
        super().__init__(name, age, weight)
        self.egg_count = egg_count
    
    def make_sound(self):
        return "Bawk-Bawk!"
    
    def lay_egg(self):
        self.egg_count += 1
        return f"{self.name} laid an egg. Total eggs: {self.egg_count}"

class Horse(Animal):
    
    def __init__(self, name, age, weight, running):
        super().__init__(name, age, weight)
        self.running = running
    
    def make_sound(self):
        return "Neeeiigh!"
    
    def speed_run(self):
        return f"{self.name} maximum speed is {self.running} km/h "
if __name__ == "__main__":
    cow = Cow("Maria", 5, 500, 10)
    chicken = Chicken("Nastiya", 1, 3, 2)
    horse = Horse("Chaqmoq", 3, 85, 45)
    
    print(cow.eat())
    print(cow.make_sound())
    print(cow.produce_milk())
    
    print(chicken.eat())
    print(chicken.make_sound())
    print(chicken.lay_egg())
    
    print(horse.eat())
    print(horse.make_sound())
    print(horse.speed_run())