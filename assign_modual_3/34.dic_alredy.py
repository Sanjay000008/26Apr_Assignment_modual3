#Write a Python program script to check if a given key alredy exists in a dictionary.
dic={}
n=int(input("Enter Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    dic[key]=value
print(dic)
x=input("Enter Key:-")
if x in dic:
    print("Key Alredy Exist")
else:
    print("Key Is not Present")