"""Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. """

str= 'w3resource' 
dic = {}
for i in str:
    dic[i] = dic.get(i, 0) + 1
print(dic)