#Write A Python script to print a dictionary where the keys are numbers between 1 and 15
dic={}
n=int(input("Enter Your Number  Between 1 to 15:-"))
for i in range(1,n+1):
    dic[i]= i*i
print(dic)  