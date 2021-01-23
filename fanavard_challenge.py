import sys,math,random

#creating an empty list
lst1 = []
m = int(input("Enter number of box:"))
k = int(input("Enter size of box:"))
#adding the size of boxs to list
for d in range(0,m):
    lst1.append(k)
    
#creating an empty list    
lst2 = []
n = int(input("Enter number of things:"))
#adding the size of things to list
for i in range(0,n):
    a = int(input("Enter size of things :"))
    lst2.append(a)
#out put    
print(m,k,n)
print(lst1)
print(lst2)

#Calculate the number of objects placed in boxes
for c in range(len(lst1)):
    if lst1[c] != 0 :
        for j in range(len(lst2)):
            if lst2[j] <= lst1[c]:
                lst1[c] = lst1[c] - lst2[j]
                j += 1
            else:
                continue
print(j)
