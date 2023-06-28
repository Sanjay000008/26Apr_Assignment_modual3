#Write a Python program to check whether an element exists within a tuple
t=tuple()
n=int(input("Enter Number Of Tuple Data:-"))
for i in range(n):
    x=int(input("Enter Tuple Item:-"))
    t +=(x,)


e=int(input("Enter An Elements to chek :-"))
if e in t:
    index=t.index(e)
    print("Elements found in tuple as index",index)
else:
    print("Data not found in tuple")
