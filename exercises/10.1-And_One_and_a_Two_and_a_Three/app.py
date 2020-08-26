contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
some=""
for key in contact:
    some=some + (key + " : " + contact[key] +"\n")
print(some)