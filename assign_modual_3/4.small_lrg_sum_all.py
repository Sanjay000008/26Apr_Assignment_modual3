#Write a Python function to get the largest number, smallest num and sum of all from a list


data=list()
n=int(input("Enter Numer of Value:-"))
for i in range(n):
    s=int(input("Enter Number:-"))
    data.append(s)
print(data)
data.sort()
print("Smallest Number:-",data[0])
print("Largest Number:-",data[-1])
total=0
for i in data:
    total= total + i
print("Sum of all Elements of list is:-",total)