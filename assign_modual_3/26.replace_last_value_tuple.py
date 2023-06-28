#Write a Python program for replace last value of tuples in a list.
data=[]
n=int(input("Enter Number Of Data:-"))
for i in range(n):
    d=input("Enter Your Data:-")
    data.append(d)
print(data)
data.pop()
t=input("Enter Last Value:-")
data.append(t)
print(tuple(data))
    


