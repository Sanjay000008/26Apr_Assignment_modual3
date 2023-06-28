#Write a Python program to remove duplicates from a list

data=[]

n=int(input("Enter A number Of Data:-"))
for i in range(n):
    x=input("Enter Value:-")
    if x not in data:
        data.append(x)

print(data)
