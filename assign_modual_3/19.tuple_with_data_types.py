#Write a Python program to create a tuple with different data types.
data=[]
n=int(input("Enter Number of Data:-"))
for i in range(n):
    x=input("Enter Your Data:-") 
    data.append(x)
print(tuple(data))
"""d=list(map(type,data))
print(d)
"""
d=tuple(data)

for i in d:
    print(type(i))