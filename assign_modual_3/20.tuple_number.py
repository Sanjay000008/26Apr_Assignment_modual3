#Write a Python program to create a tuple with numbers
data=[]
n=int(input("Enter Number Of Data:-"))
for i in range(n):
    s=int(input("Enter Data:- "))
    data.append(s)
print(tuple(data))