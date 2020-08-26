theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def boolCheck(boole):
    if boole==0:
       return "woko"
    elif boole==1:
        return "wiki"
print(list(map(boolCheck,theBools)))
