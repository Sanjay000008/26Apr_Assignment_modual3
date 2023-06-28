#How will you compare two lists

l1=[]
l2=[]
l3=[]
n=int(input("Enter number of value1:-"))
for i in range(n):
    s=input("Enter Your Value:-")
    l1.append(s)

d=int(input("Enter Number Of Value2:-"))
for j in range(d):
    x=input("Enter Your Value:-")
    l2.append(x)
print(l1)
print(l2)

for n in l1:
    if n in l2:
        if n not in l3:
            l3.append(n)
print(l3)



