#Write a Python program to create and display all combinations of letters,selecting
#each letter from a different key in a dictionary.
#Sample Data:{'1':['a','b'],'2':['c','d']}
#output:ac ad bc bd

d={'1':['a','b'],'2':['c','d']}
l=list(d.values())
for comb in l[1:]:
    for i in l[0]:
        for j in comb:
            print(i+j)

