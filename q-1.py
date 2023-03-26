import json
file = open("C:\\Users\\Admin\\Desktop\\data science\\Assignment_6\\employee.json",'r')
data = file.read()
file.close()
user = json.loads(data)
print(user)