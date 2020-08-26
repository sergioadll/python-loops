people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    newpeople=[]
    for x in people:
        if x!=person_name:
            newpeople.append(x)
    return newpeople
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))