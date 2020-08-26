
#Your code go here:
x=20
result=""
while x>0:
    if x%5==0:
        result=result+ str(x)+"!\n"
    else:
        result=result + str(x) +"\n"
    x-=1
print(result+"LISTOFF")