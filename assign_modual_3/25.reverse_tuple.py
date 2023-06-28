#Write a Python program to reverse a tuple.
t=[]
n=int(input("Enter Number Of Data:-"))
for i in range(n):
    x=input("Enter your Data:-")
    t.append(x)
print(t)
t.reverse()
d=tuple(t)
print(d)

