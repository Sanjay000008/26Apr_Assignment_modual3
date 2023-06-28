#Write a Python program to convert a tuple to a string.
data=[]


s=int(input("Enter Numbrer of Charactars:-"))
for i in range(s):
    x=input("Enter Word:-")
    data.append(x)
print(tuple(data))
str="".join(data)
print(str)