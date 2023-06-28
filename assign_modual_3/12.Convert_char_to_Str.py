#Write a Pythin program to convert a list of characters into a string

data=[]


s=int(input("Enter Numbrer of Charactars:-"))
for i in range(s):
    x=input("Enter Word:-")
    data.append(x)
    str="".join(data)
print(str)