import json

indian_state = {
             "Gujarat": "Gandhinagar",
             "Maharashatra": "Mumbai", 
             "Karnataka": "Bengaluru", 
             "Punjab": "Chandigarh",
             "Chattishgarh": "Raipur",
             "Bihar": "Patna", 
             "Goa": "Panji"
             }
data= json.dumps(indian_state)
file = open('indian_States.json','w')
file.write(data)
file.close()
