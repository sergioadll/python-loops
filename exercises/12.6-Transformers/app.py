incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
transformedData=""

def my_var(arg):
    transformedData=arg["name"]+" "+arg["lastName"]
    return transformedData
print(list(map(my_var,incomingAJAXData)))

