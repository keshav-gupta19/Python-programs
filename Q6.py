#Ques 6
c=int(input("Enter the first element."))
h=int(input("Enter the second element."))
b=[]
for i in range(c,h+1):
    a=0


    for j in range(2,i//2+1):
        if i%j==0:
            a=a+1
            break
    if (a==0 and i!=1):
        print("%d" %i,end='  ')
    
    

    
            
