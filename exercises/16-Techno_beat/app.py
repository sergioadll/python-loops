def lyrics_generator(beat):
    beatList=[]
    n=" "
    for x in beat:
        if x==0:
            beatList.append("Boom")
        elif x==1:
            beatList.append("Drop the base")
        if len(beatList)>=3 and beatList[-3:].count("Drop the base")==3:
            beatList.append("!!!Break the base!!!")
    
    return n.join(beatList)


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))