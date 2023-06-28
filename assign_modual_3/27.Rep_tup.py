#Write a Python program to find the repeated items of a tuple
data=[]
n=int(input("Enter Number of data:-"))
for i in range(n):
    d=input("Enter Your Data:")
    data.append(d)
print(tuple(data))
l=[]
for x in data:
        if data.count(x) > 1:
            if x not in l:
                l.append(x)
print(l)