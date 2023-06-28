#Write a Python program to chek wether a list countains a sub list

list=[]
n=int(input("Enter number of data:"))
for i in range(n):
    x=input("Enter Your Data:")
    list.append(x)
data=[]
d=int(input("Enter Number of data:"))
for i in range(d):
    y=input("Enter Your Data:-")
    data.append(y)
print(data)
list.append(data)
print(list)
if data in list:
    print("Sublist In List")
elif y not in data:
    print("No Sub List in List")