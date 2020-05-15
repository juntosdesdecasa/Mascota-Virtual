# Code example from the workshop "Crea tu propia mascota virtual" for "Juntos desde casa" initiative

print("Bienvenido")

# Setting different types of variables for the Pypet
name = "Pymoai"
age = 5
weight = 3.5
hungry = True
photo = "(=^o.o^=)__"

# Showing variables
print("Hola, me llamo " + name)
print(photo)

# Ordering the pypet features as a dictionary
cat = {
  'name': "Pymoai",
  'age': 5,
  'weight': 3.5,
  'hungry': True,
  'mood':"neutral",
  'photo': "(=^o.o^=)__"
}

# Adding a new pet as a dictionary
mouse = {
  'name': "Pymoo",
  'age': 3,
  'weight': 2.5,
  'hungry': True,
  'mood': "neutral",
  'photo': "<:3 )---"
}

# Showing features in the dictionaries through their keys
print(cat['name'])
print(cat['photo'])
print(mouse['name'])
print(mouse['photo'])

# Defining a function for feeding our pypet only if it is hungry
def feed(pet):
  if pet['hungry']== False:
    print("No tengo hambre")
  else: 
    pet['hungry']= False
    pet['weight']= pet['weight'] + 0.5 

# Creating a list (another python data structure) for ordering our pets
pets = [cat, mouse]

# Example of a "for loop" in which we feed all the pets belonging to the pets list 
for pet in pets:
  feed(pet)
  print("Has dado de comer a ")
  print(pet['name'])

# Defining a function for making our pets play together
def play(pet_list):

  for pet in pets:

    if pet['weight']> 2:
      pet['mood']= "happy"
      pet['weight']= pet['weight'] - 0.5
    else:
      pet['hungry']= True
      print(pet['name'])
      print("está demasido débil para jugar") 

# Making our virtual pets play
play(pets)
print("Tus mascotas han jugado un rato")
print("Su estado es ", cat['mood'])

# Including interaction by input through keyboard for feeding or playing
print("Introduce 'comer' para alimentar a tu mascota y 'jugar' para que jueguen")
orden = input("¿Qué quieres hacer? ")

if orden == "comer":
  feed(cat)
elif orden == "jugar":
  play(pets)
else:
  print("Introduce 'comer' o 'jugar'")    

# Showing final state of two dictionaries
print(pets)