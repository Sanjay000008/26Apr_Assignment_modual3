#Write a Python program to count the number of strings where the string 
#length is 2 or more and the first and last character are same from a given 
#list of strings
w1=[]
s=int(input("Enter Number of Srting:-"))

for i in range(s):
    x=input("Enter Your String:-")
    w1.append(x)
print(w1)
count=0
for w in w1:
    if len(w)>1 and w[0]==w[-1]:
        count+=1
print(count)