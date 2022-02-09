def find(arr,n):
    arr=sorted(arr)
    Max=arr[n-1]
    table=[10**9 for i in range((2*Max+1))]
    table[0]=0
    ans=-1
    for i in range(1,2*Max+1):
        for j in range(n):
            if arr[j]<=i:
                res=table



arr=list(map(int,input().split()))

print(find(arr,len(arr)))
