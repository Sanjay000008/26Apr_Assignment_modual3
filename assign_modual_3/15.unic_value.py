#Write a Python Program to get unique values from a list
list=[]
n=int(input("Enter Number Of Data:-"))
for i in range(n):
    x=input("Enter Number Of Value:-")
    list.append(x)
print(list)
data=[]
for a in list:
    if a not in data:
        data.append(a)
print(data)

