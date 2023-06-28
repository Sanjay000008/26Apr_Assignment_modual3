# What is List?How will you reverse a list?

# List are used to store multiple items in a single variable.
# List is bult-in data types in python used to store collaction of data.

data=list()
n=int(input("Enter Number Of Value:-"))
for i in range(n):
    s=input("Enter Your Data:-")
    data.append(s)

print(data)
data.reverse()
print(data)

