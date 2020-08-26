arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
newArr=[]
leng=len(arr)-1
for i in range(leng,-1,-1):
    newArr.append(arr[i])
print(newArr)