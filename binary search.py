def bin(arr,l,r,x):
    mid=(l+r)//2
    if l<=r:
        if x==arr[mid]:
            return mid
        elif x>arr[mid]:
            return bin(arr,mid+1,r,x)
        else:
            return bin(arr,l,mid-1,x)
    else:
        return -1
    
arr=[1,2,3,4,5]
x=3
res=bin(arr,0,len(arr)-1,x)
if res==-1:
    print(x,"is not present")
else:
    print(x,"is found at index",res)
