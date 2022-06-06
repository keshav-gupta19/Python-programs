#Ques 8
a=input("Enter the string")
d=0
for i in range(0,len(a)):
    if a[i].isdigit():
        d+=int(a[i])
print("The number after adding:",d)    
    
