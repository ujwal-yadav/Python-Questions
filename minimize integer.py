s="1399"
K=4
if int(s[0])==1 and K==len(s):
    K-=1
s=list(s)
op=0
i=0
while op<K:
    if i==0 and int(s[i])!=1:
        s[i]="1"
        op+=1
    if i>0 and int(s[i])!=0:
        s[i]="0"
        op+=1
    i+=1
    
s=int("".join(s))
print(s)
