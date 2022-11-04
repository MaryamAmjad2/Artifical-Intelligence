#task1

list1=[]
list2=[]
for i in range (0,4):
    n = int(input("enter a number"))
    list1.append(n)

for j in range (0,4):
    n = int(input("enter a number"))
    list2.append(n)
list3=list1+list2
print(list3)
for m in range(0,len(list3)-1):
    for k in range(0,len(list3)-1):
            if(list3[k]>list3[k+1]):
               temp=list3[k]
               list3[k]=list3[k+1]
               list3[k+1]=temp

print(list3)


#task2

large=list3[0]
for i in range (1,len(list3)):
    if(list3[i]>large):
        large=list3[i]
print(large)

small=list3[0]
for i in range (1,len(list3)):
    if(list3[i]<small):
        small=list3[i]
print(small)



#Task 3
import math 
from math import *
x=float(input("enter x"))
h=0.001
m=(sin(x+h)-sin(x))/h
n=cos(x)
m=math.ceil(m*100)/100
n=math.ceil(n*100)/100
if(math.isclose(m,n)):
    print("Equal")
else:
    print("Not Equal")
print(m)
print(n)


#task 4:
birthday={("Maryam"):"23 june 2002",("Ayesha"):"12 july 2002",("Sarah"):"4 december 2002"}
print("Welcome to the birthday Dictionary. We know birthday of ")
for key, value in birthday.items():
    print(key)
n =input("Whose Birthday do you want to know")
n=n.capitalize()
if n in birthday:
    print(birthday[n])
else :
    print("NO Result")






#task5:
smaple={"name":"kelly","age":"20","Salary":"200000","city":"Lahore"}
keys=["name","age"]
dic2=dict()
for i in keys:
    dic2.update({i:smaple[i]})
print(dic2)








