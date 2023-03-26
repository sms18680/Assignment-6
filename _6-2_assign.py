# Assignment 2
# 👉 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.
class dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print('tuffy')
        print('10')
    def display(self):
        print('tuffy')
        print('10')
    def get_info(self):
        print('blue')
    def display(self):
        print('blue')
class JackRussellTerrier(dog):
    def __init__(self,food,place):
        self.food = food
        self.place = place
    def display(self):
        print('peddy')
        print('forest')
class BullDog:
    def __init__(self,action,voice):
        self.action=action
        self.voice=voice
    def display(self):
        print('wild')
        print('woof')
obj = dog('tuffy',10,'blue')
obj.description()
obj.get_info()
obj1=JackRussellTerrier('peddy','forest')
obj1.display()
obj2=BullDog('wild','woof')
obj2.display()