#Ques 3
def operators(x,operator,y):
    if (operator=='+'):
        print(x+y)
    elif (operator=='-'):
        print(x-y)
    elif (operator== '*'):
        print(x*y)
    elif (operator== '/'):
        print(x/y)
    elif (operator=='or'):
        print(x or y)
    else:
        print("Choose Any of the operators (+,-,*,/,or,and)")

x=int(input())
op=input()
y=int(input())
operators(x,op,y)