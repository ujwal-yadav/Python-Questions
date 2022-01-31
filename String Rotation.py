def rotate(string,number):
    if number%2==0:
        revstr=list(string)
        revstr=revstr[-1:]+revstr[:-1]
        return revstr
    else:
        revstr=list(string)
        revstr=revstr[2:]+revstr[:2]
        return revstr

inp=['abcde:234','pqrs:246']
st=[]
num=[]
for i in inp:
    s,n=i.split(":")
    st.append(s)
    num.append(n)

for i in range(len(num)):
    x=list(str(num[i]))
    add=0
    for j in range(len(x)):
        add=add+int(x[j])**2
    rev=rotate(st[i],add)
    rev="".join(rev)
    print(rev)
