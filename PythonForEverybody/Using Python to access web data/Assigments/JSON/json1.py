import json 
#json represents data as nested dictionaries
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data) #info is a dictionary
print('Name: ', info["name"])#info["name"] es Chuck
print('Hide: ', info["email"]["hide"])#info["email"] is another dictionary
print('Phone: ',info["phone"]["number"])
