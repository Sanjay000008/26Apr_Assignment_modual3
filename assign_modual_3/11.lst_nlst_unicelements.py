#Write a Python function that takes a list and returns a new list with unique 
#elements of the first list

def ul(d):
    x=[]
    for m in d:
        if m not in x:
            x.append(m)
    return x
        
dl=[]
n=int(input("Enter Number of List:-"))
for i in range(n):
    s=input("Enter Your List Value:- ")
    dl.append(s)
print("Origanal List:-",dl)
print(ul(dl))