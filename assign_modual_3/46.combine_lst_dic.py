"""Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output:
Counter ({'item1': 1150, 'item2': 300})"""


"""n=int(input("How Many List You Wan't:-"))
for i in range(n):
    t={}
    key=['item','amount']
    for j in range(len(key)):
        value=input(f"Enter Youe Value For {key[j]} :-") 
        t[key[j]]=value
    d.append(t)"""

from collections import Counter
d = [ {'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
    300},{'item': 'item1', 'amount': 750}]

r = Counter()
for i in d:
    r[i['item']] += i['amount']
print(r)