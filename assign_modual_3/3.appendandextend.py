#Differentiate between append() and extend() Methods.
# Append:- is used to the at the aliment end of the list. if you want to add single element you can used append
# Extend :- is used to the at the aliment end of the list. 
#but is you give any string like a.extend(sanju) in this case each charactor taken as the elements 
#in extend method we have already have a list we make new list than we can used extend method to merge data.

data=list()
n=int(input("Enter Number Of Data:-"))
for i in range(n):
    s=input("Enter Value:-")
    data.append(s)
print(data)

ndata=list()
p=int(input("Enter Number Of Data:-"))
for j in range(p):
    r=input("Enter Value:-")
    ndata.append(r)
print(ndata)

data.extend(ndata)
print(data)

 