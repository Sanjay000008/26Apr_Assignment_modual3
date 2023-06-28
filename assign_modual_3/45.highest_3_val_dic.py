#Write a Python program to find the highest 3 values in a dictionary
d={}
key=['a','b','c','d','e','f']
for i in range(len(key)):
    x=int(input(f"Enter Only Number for {key[i]} :-"))
    d[key[i]] = x
print(d)

lrg=sorted(d, key=d.get, reverse=True)
for i in range(3):
    print(lrg[i])