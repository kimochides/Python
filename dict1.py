thisdict={"brand":"Ford",
          "model":"Mustang",
          "year":1964}
thisdict2=dict(name="John",age=36,country="Norway")
print(thisdict)
print(thisdict2)

#creating an empty dictionary
my_dict={}

#Adding key-value pairs to the dictionary
my_dict['name']='Alice' 
my_dict['age']=30
my_dict['city']='New York' 

print("Initial dictionary:",my_dict)
print(len(my_dict))
print(type(my_dict))

#Accessing
print("Name:",my_dict['name'])
print("Age:",my_dict['age'])
x=my_dict.keys()
print(x)
y=my_dict.values()
print(y)
z=my_dict.items()
print(z)
m=my_dict.get("city")
print(m)

#modifying
my_dict['age']=35
print("Modified age:",my_dict['age'])

my_dict.update({"age":45})

#adding to the dictionary
my_dict["color1"]='fair'
print(my_dict)

my_dict.update({"color2":"dark"})

#removing a key-value pair
removed_value=my_dict.pop('city')
print(removed_value)
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.clear()
print("Dictionary after clearing:",my_dict)

del my_dict
