#Ques 2---> To print the secured credit card number.
def creditcard(a):
    c=""
    for i in range(0,len(a)):
        if i>=len(a)-4:
            c+=a[i]
        else:
            c+='*'
    return c        

a=input("enter your cerdit card number :")
d=creditcard(a)
print("the result is :",d)
