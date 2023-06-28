#Write a Python script to concatenate following dictionaries to create a new one.
dic={}
n=int(input("Frist Dictionary Number Of Pairs:-"))
for i in range(n):
    key=int(input("Enter Number Of Key's:-"))
    value=int(input("Enter Number Of Value:- "))
    dic[key]=value


dic1={}
n=int(input("Second Dictionary Number Of Pairs:-"))
for i in range(n):
    key=int(input("Enter Number Of Key's:-"))
    value=int(input("Enter Number Of Value:- "))
    dic1[key]=value


dic2={}
n=int(input("Third Dictionary Number Of Pairs:-"))
for i in range(n):
    key=int(input("Enter Number Of Key's:-"))
    value=int(input("Enter Number Of Value:- "))
    dic2[key]=value

print("Dic:-",dic)   
print("Dic1:-",dic1) 
print("Dic2:-",dic2)


dic3={}
for d in (dic,dic1,dic2):
    dic3.update(d)
print(dic3)
