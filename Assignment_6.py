# # # Create an assignment for File handling of JSON files in Python
# # # Assignment 1
# # # 👉 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information 
# # #       consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and 
# # #       saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.
# import json

# size = int(input("enter employee no"))
# data = {}
# lst = []

# for i in range(size):
#     data = {}
#     name = input("Enter your name :")
#     dob = (input("Enter your dob :"))
#     height =(input("Enter your height"))
#     city = input("Enter your city name") 
#     state = input("Enter your state name")
#     data["naam"] = name
#     data["dob"]= dob
#     data["height"] = height
#     data["city"] = city
#     data["state"] = state
#     lst.append(data)
# file = open("C:\\Users\\Admin\\Desktop\\data science\\class_super()\\final project\\assignment-6.json", 'w')
# json.dump(size,file) 





# # # 👉 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
# import json
# dict_obj= {
#      "Gujarat" : "Gandhinagar", "Maharashatra" : "Mumbai",
#      "Karnataka" : "Bengaluru", "Punjab": "Chandigarh",
#      "Chattishgarh" : "Raipur", "Bihar": "Patna",
#      "Goa" : "Panji"
#        }
# json_obj = json.dumps(dict_obj)
# print(json_obj)


# # # Assignment 2
# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
#     You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. 
# It should have at least two methods of its own.
#  d. Create objects and implement the above functionalities.

class dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
    def description(self):
        print('name', self.name)
        print('age', self.age)
    def get_info(self):
        print('coat_color', self.coat_color)
class JackRussellTerrier(dog):
    def __init__(self,food,place):
        self.food=food
        self.place=place
    def display(self):
        print('food',self.food)
        print('place',self.place)
class Bulldog(JackRussellTerrier):
    def __init__(self,action):
        
        self.action=action
    def display(self):
        print('action',self.action)

obj=dog('tuffy',12,'blue')
obj.description()
obj.get_info()
obj1=JackRussellTerrier('paddy','forest')
obj1.display()
obj2=Bulldog('woof')
obj2.display()

   






