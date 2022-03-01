s="001"
count=0
n=len(s)
for i in range(n):
    for j in range(i+1,n+1):
        k=s[i: j]
        if k==k[::-1]:
            count+=1
    
print(count)
