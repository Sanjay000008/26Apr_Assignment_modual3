#Write a Python program to remove empty tuple(s) from a list of tuples.
n=int(input("Enter Number Of Tuple:-"))
data=[]
for i in range(n):
    st=[]
    v=int(input("Enter Number Of Tuple Data:-"))
    if v==0:
        break
    for d in range(v):
        t=input("Enter Your Value:")
        st.append(t)
        s=tuple(st)
    data.append(s)
print(data)


            
   

