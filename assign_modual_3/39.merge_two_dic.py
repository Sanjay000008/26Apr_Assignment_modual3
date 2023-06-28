#Write a Python script to merge two python dictionaries.

dic={}
n=int(input("Enter Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    dic[key]=value
print(dic)

dic1={}
n=int(input("Enter Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    dic1[key]=value
print(dic1)
dic.update(dic1)
print(dic)