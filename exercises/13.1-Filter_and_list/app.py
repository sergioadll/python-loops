
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def func(name):
     if name.startswith("R"):
         return name
resulting_names = list(filter(func, all_names))
print(resulting_names)




