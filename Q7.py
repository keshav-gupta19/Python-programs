#Ques 7
import statistics
a=int(input("Enter the size of array :"))
b=[]
print("Enter the numbers :")
for i in range(0,a):
    c=input()
    b.append(c)
    
d=statistics.mode(b)
print("The most occuring element in the array is ",d)

    
    
