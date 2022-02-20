import itertools
arr=list(map(int,input().split(" ")))
arr=sorted(arr)
m=0

for i in range(len(arr)):
    lst=list(itertools.combinations(arr,len(arr)-i))
    for j in lst:
        s=sum(j)
        if s%2!=0:
            m=max(m,s)
print(m)
