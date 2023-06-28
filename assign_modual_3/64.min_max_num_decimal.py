# Write a Python program to find the maximum and minimum numbers 
#from the specified decimal numbers. 

d=[]
n=int(input("Enter Number of list Data:-"))
for i in range(n):
    x=float(input("Plz Enter Only Decimal Number:-"))
    d.append(x)
print(d)
print("-----------------------------------------")
print("Maximum Value Of decimal Number:-",max(d))
print("-----------------------------------------")
print("Minimum Value Of Decimal Number:-",min(d))
