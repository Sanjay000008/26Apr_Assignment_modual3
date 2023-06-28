#Write a Python program to check a list is empty or not

el=[]
n=int(input("Enter Number of data:-"))
for i in range(n):
    e=input("Enter value:-")
    el.append(e)
print(el)
if not el:
    print("List is Empty")
else:
    print("List is Filluped")