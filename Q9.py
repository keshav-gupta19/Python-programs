#Q9
a=input("Enter the string") #Taking input
d=[]
b=""
for i in range(0,len(a)): #Entering the values into list.
    d.append(a[i])
d.sort() #Sorting
for i in d:
    b+=i
print(b)  #Output
    
