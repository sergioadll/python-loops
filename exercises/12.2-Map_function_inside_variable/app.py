names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']
lista=[]
def prepender(name):
    return "My name is: " + name
#Your code go here:
lista=list(map(prepender, names))
print(lista)