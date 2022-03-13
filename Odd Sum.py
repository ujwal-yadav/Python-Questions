import itertools
arr=list(map(int,input().split(" ")))
arr=sorted(arr)
ma=0

for i in range(len(arr)):
    lst=list(itertools.combinations(arr,len(arr)-i))
    for j in lst:
        s=sum(j)
        if s%2!=0:
            ma=max(ma,s)
print(ma)
