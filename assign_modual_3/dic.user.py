mydic={}

keys=['id','name','city']

for i in range(len(keys)):
    value=input(f"Enter Your Value for {keys[i]}:-")
    mydic[keys[i]]=value
print(mydic)