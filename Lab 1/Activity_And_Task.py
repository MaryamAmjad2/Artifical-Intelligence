
                  
         

#Activity1         
        
n=int(input('Enter a number '))
if( n%2==0):
    print('Even')
else:
    print('ODD')

#Activity 2

summ=0
n = int (input("Enter numbers"))
while n!=0 :
         summ=summ+n
         n= int (input("Enter numbers"))
print (summ)

#Activity 3

s = int (input('Enter a number'))
if s >2:
    if s%2==0 :
        print('Not prime')
    else :
        print('Prime')
else:
    print('Prime')

#Activity 4

summ=0
for i in range(0,5):
    n = int(input("enter number "))
    summ=summ+n
print('Sum is',summ)

#Activity 5

a = 1
summ=0
while(a<=10):
    summ=summ+a
    a=a+1
print(summ)

#Activity 6

name = input ("enter your Name")
age =  input ("enter your age")
education= input ("enter your education")
print('Hello, Your Name is ',name,'Your age is ',age ,'your education is ',education)

#Activity 7


import random
MAXIMUM=1
MINIMUM=9
num=random.randint(MAXIMUM,MINIMUM)

tryy=0
Running=True
while(Running):
    inp=input("Enter Number")
    if(inp.lower()=='exit'):
        Running=False
        print("Exiting Game")
    elif num >int(inp):
        print("LOW")
    elif num< int(inp):
        print("HIGH")
   
    
    elif num==int(inp ):
        print(" You Gussed Right")
        if(tryy<2):
            print("Impressive")
        else:
            print("Better Luck Next Time")
    
    tryy=tryy+1
        



#Lab Task 1

num = int(input("enter a Number"))
if(num>0):
    rem=num%10
    rev=0
    rev=rem+(rev*10)
    num=num//10
    print(rem,num)

else:
    print("Not Valid")


#Lab Task 2

sume=0
sumo=0
for i in range(0,6):
    n = int(input("Enter Number"))
    if(n%2==0):
        sume=sume+n
    else:
        sumo=sumo+n
print( 'sum of even is ',sume)
print('sum of odd is' ,sumo)



#Lab Task 3

n = int(input("enter number "))
a=0
b=1
for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

#Lab Task 4

num = int (input("Enter number "))
if(num<=100 and num>=0):
           if(num<50):
               print("F")
           elif(num>=51 and num<=60):
               print("E")
           elif(num>=61 and num<=70):
               print("D")
           elif(num>=71 and num<=80):
               print("C")
           elif(num>=81 and num<=90):
               print("B")
           elif(num>=91 and num<=100):
               print("A")
else:
    print("INVALID")



#Lab Task 5


num = int (input("Enter number "))
fac=1
if(num>1):
    while(num>1):
        fac=fac*num
        num=num-1
    print(fac)
else:
    print(1)
