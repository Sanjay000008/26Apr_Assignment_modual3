 #write a Python program to select an item randomly from a list.and
import random
data=[]
n=int(input("Enter Number Of data:"))
for i in range(n):
    x=input("Enter Your Data:")
    data.append(x) 
print(data)
y="y"
while y!="n":
    x=random.choice(data)
    print(x)
    y=input("Refresh:")
    


