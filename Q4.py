#Ques 4
def stringfunction(a):
    c=""
    for i in range(0,len(a)):
        c+=2*a[i]
    return c    

a=input("Enter the string: \n")
b=stringfunction(a)
print("The result of the operation is ",b)

