#Ques 5
a=[]
for i in range(0,100):
    x=int(input())
    a.append(x)
ans=0
for i in range(100):
   for j in range(i+1,100):
       if (a[i]==a[j]):
           print(a[i])
           ans=ans+1
           break
   if ans==1:
        break