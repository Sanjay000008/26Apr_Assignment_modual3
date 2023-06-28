#Write a Python program to convert a list of tuples into a dictionary.
def dic(data):
    return dict(data)

n=int(input("Enter Number Of Tuple:-"))
data=[]
for i in range(n):
    st=[]
    v=int(input("Enter Number Of Tuple Data:-"))
    for d in range(v):
        t=input("Enter Your Value:")
        st.append(t)
        s=tuple(st)
    data.append(s)
print(data)
print(dic(data))
