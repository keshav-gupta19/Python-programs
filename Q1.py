#Ques 1--> To do the sorting according to the given question. 
def func1(d,e):
    if e=="asc":
        d.sort()
        return d
    elif e=="desc":
        d.sort(reverse=True)
        return d
    else :
        return d
    
a=int(input("Enter the total number of elements which you want to enter in the array :")) #NUMBER OF ELEMENTS IN AN ARRAY
d=[]
print("Start inputing elements") #TAKING THE INPUTS
for i in range(0,a):#appending the elements in array
    c=input()
    d.append(c)
e=input("enter what do you want to do with array 1.asc  , 2. desc , 3. none :")

f=func1(d,e)
print("the result is :",f)
    
    
