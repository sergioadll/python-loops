#Import random
import random
#Create the function below:
inte=random.randint(1,5)
entero=inte
row=[]
matrix=[]
def matrixBuilder(entero):
    for i in range(entero):
       row.append(1)
    for i in range(entero):
        global matrix
        matrix.append(row)
    return matrix
print(matrixBuilder(entero))
