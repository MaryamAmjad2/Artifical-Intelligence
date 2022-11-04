


    

#task :1 join of two list
list1=[]
list2=[]
list3=[]
for i in range (0,5):
    n = input("Enter input for list 1 ")
    list1.append(n)
for i in range (0,5):
    n = input("Enter input for list 2 ")
    list2.append(n)
list3=list1+list2
print(list3)


#task 2 :PALINDROME
n= input("Enter a string")
n=n.upper()
print(n)
m=n[::-1]
print(m)
if(m==n):
    print("IS PALINDROME")
else:
    print("NOT PALINDROME")



#task :3
list1=[[1,2,3],[2,3,4]]
list2=[[3,4,5],[2,4,9]]
list3=[[0,0,0],[0,0,0]]
for i in range (2):
    for j in range (2):
        for k in range (2):
            list3[i][j]+=(list1[i][j]*list2[i][j])

print(list3)



#task 4:
def perimeter( list):
    length=len(list)
    perimeter=0
    for i in range (0,length-1):
        distance=((list[i][0]-list[i+1][0])**2)+((list[i][1]-list[i+1][1])**2)**0.5
        perimeter=perimeter+distance
    perimeter=perimeter+ ((list[0][0]-list[length-1][0])**2)+((list[0][1]-list[length-1][1])**2)**0.5
    return perimeter
L=[(2,4),(3,7)]
print(perimeter(L))



#task 5:
n =[2,3,5,7,1,2,3,6]
m=[1,4,6,8,0,2,4,5]
e=set()
for i in n:
    if i not in m :
        e.add(i)
print("A-B",e)
for i in m:
    if i not in n :
        e.add(i)
print("B-A",e)


#task 6:
sample={("Maryam","Amjad"):"0909092",("Sarah","khan"):"989982",("Ayesha","Malik"):"8898982"}
fname=input("Enter first Name").capitalize()
Lname=input("Enter Last Name").capitalize()
h=(fname,Lname)
if h in sample:
    print(sample[h])
else:
    print("No DATA")
