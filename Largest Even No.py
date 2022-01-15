st="QWert@821142"
temp="";
s=""
for i in st:
    if i.isdigit():
        temp=temp+i;
temp=sorted(temp,reverse=True)
for j in range(len(temp)):
    if(j!=len(temp)-1 and temp[j]==temp[j+1]):
        continue;
    else:
        s=s+temp[j];
temp=list(s)

l=len(temp);
for i in reversed(range(l)):
    if int(temp[l-1])%2!=0:
        temp[l-1], temp[i-1] = temp[i-1], temp[l-1];
    else:
        continue;

temp = int(''.join(map(str, temp)))
print(temp);
