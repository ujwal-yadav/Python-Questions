T=list(map(int,input("").split()))
N=T[1:]
for i in N:
    arr=[1,6,0*i]
    i=i-1
    if i > 1:
        arr[i]=((arr[i-1]+2)*2-arr[i-2])
    print(arr[i]%10**(9+7),end=" ")
