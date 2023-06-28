#Write a Python program to convert List into Tuple
list=[]
n=int(input("Enter Number Of Data:-"))
for i in range(n):
    d=input("Enter your data:-")
    list.append(d)
print(list)
print(tuple(list))