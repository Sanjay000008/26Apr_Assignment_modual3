#Write a Python program to print all unique value in dictionary
d={}
n=int(input("Enter Number Of Dict Data:-"))
for i in range(n):
    key=int(input("Enter Only Number:-"))
    value=input("Enter Your Value:-")
    d[key]=value

print(d)
print("-------------------------------")
print(set(d.values()))