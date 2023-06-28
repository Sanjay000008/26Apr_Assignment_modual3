#Write a Python program to find the length of a tuple
data=[]
n=int(input("Enter Number Of Tuple Data:-"))
for i in range(n):
    x=input("Enter Your Data:-")
    data.append(x)
print(tuple(data))
print(len(data))