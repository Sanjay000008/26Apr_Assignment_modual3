#How will you remove last object from list?
# We can use List.pop function to remove last object and one another way is
# we can used del list[-1] we can remove last objest of list


"""s=[2,33,222,14,25]
print(s)
print(s[-1])
#s.pop()
del s[-1]
print(s)"""

# user input program
d=list()
a=int(input("Enter a Number Of value:-"))
for i in range(a):
    s=input("Enter Your data:- ")
    d.append(s)
print(d)
print(d[-1])
#d.pop()
del d[-1]
print(d)