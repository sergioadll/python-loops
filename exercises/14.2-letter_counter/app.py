par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
par= par.lower()

counts = {}
#your code go here:
repeated={}
for char in par:
    if char != " ":
        counts[char] = par.count(char)

print(counts)

