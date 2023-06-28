#How Do You Traverse Through A Dictionary Object In Python?
dic={}
n=int(input("Enter Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    dic[key]=value
print(dic)
for i in dic:
    print(i,"----->",dic[i])