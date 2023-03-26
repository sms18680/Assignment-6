




# 👉 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
class dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print(f"\nName:{self.name}\nAge:{self.age}")
    def get_info(self):
        print("coat_color",self.coat_color)
    
class JackRussellTerrier(dog):
    def food(self):
        print('peddy')
    def place(self):
        print('forest')
class BullDog(dog):
    def action(self):
    
        print('wild')
    def voice(self):
        print('woof')

obj1 =JackRussellTerrier('tuffy',10,'black')
obj1.description()
obj1.get_info()
obj1.food()
obj1.place()
obj2=BullDog('tommy',11,'white')
obj2.description()
obj2.get_info()
obj2.action()
obj2.voice()

