from abc import ABC, abstractmethod

class Plant(ABC):
    def __init__(self, plant_name, height, age):
        self.plant_name = plant_name
        self.height = height
        self.age = age
        
    @abstractmethod
    def make_food(self):
        pass
    
    @abstractmethod
    def grow(self, height_increased, week):
        pass

class Flower(Plant):
    def __init__(self, plant_name, height, age):
        super().__init__(plant_name, height, age)
    
    def make_food(self):
        print(f"{self.plant_name} is making food.")
    
    def grow(self, height_increased = 2, week = 1):
        self.height += height_increased
        self.age += week
        print(f"{self.plant_name} grew {self.height} cm and aged {self.age} week(s).")

class Tree(Plant):
    def __init__(self, plant_name, height, age):
        super().__init__(plant_name, height, age)
    
    def make_food(self):
        print(f"{self.plant_name} is bearing fruits.")
    
    def grow(self, height_increased = 0.5, week = 1):
        self.height += height_increased
        self.age += week
        print(f"{self.plant_name} grew {self.height} m and aged {self.age} week(s).")

class Bamboo(Plant):
    def __init__(self, plant_name, height, age):
        super().__init__(plant_name, height, age)
    
    def make_food(self):
        print(f"{self.plant_name} is undergoing photosynthesis.")
    
    def grow(self, height_increased = 10, week = 1):
        self.height += height_increased
        self.age += week
        print(f"{self.plant_name} grew {self.height} cm and aged {self.age} week(s).")

print(f"Team 5 Garden")
print(f"------------------------------------------")

flower = Flower("Rose", 5, 1)
flower.make_food()
flower.grow()

print(f"------------------------------------------")

tree = Tree("Apple Tree", 10, 150)
tree.make_food()
tree.grow()

print(f"------------------------------------------")

bamboo = Bamboo("Bamboo", 100, 40)
bamboo.make_food()
bamboo.grow()