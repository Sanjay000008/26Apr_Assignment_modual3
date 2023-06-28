#How Do You Check The Presence Of A Key In A Dictionary?
# We can chekck key in dictionary to use if-in statement to check wether
# or not a given key exists in the dictionary.
dic={}
keys=[]
n=int(input("Enter Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    dic[key]=value
print(dic)

for i in dic.keys():
    print(i)
s=input("Enter Your Key:-")
if s in keys:
    print("The Key Exists")
else:
    print("Key Invalid")