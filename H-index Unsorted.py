def bs(arr):
    l=0
    r=len(arr)-1
    s=len(arr)
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid]==s-mid:
            return s-mid
        elif arr[mid]>s-mid:
            r=mid-1
        else:
            l=mid+1
    return s-l
            

arr=[2,7,1,4]
z=bs(arr)
