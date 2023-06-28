#Write a Python function that takes two lists and returns true if they have 
#at least one common member.

def cm(fi,sc):
    for i in fi:
        if i in sc:
            return True,False

n=int(input("Enter Number First List:-"))
l=[]
for i in range(n):
    s=input("Enter Your Value:-")
    l.append(s)

d=int(input("Enter Number Second List:-"))
l2=[]
for i in range(d):
    x=input("Enter Your Value:-")
    l2.append(x)

if cm(l,l2):
    print("True")
else:
    print("False")