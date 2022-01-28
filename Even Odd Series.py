import itertools
n=str(input())
s=""
for i in range(len(n)):
    if n[i].isdigit() and n[i] not in s:
        s=s+n[i]
ls=s[len(s)-1]
comb=list(itertools.permutations(s,len(s)))
m=int(''.join(comb[0]))
for i in comb:
    sx=int(''.join(i))
    temp=max(m,sx)
    if temp%2==0:
       m=temp
if m%2!=0:
    print(-1)
else:
    print(m)
