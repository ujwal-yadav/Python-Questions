arr=[1,2,3,4,5,6,7];
l=len(arr);
mid=l//2;
if l%2==0:
    arr2=arr[mid:l]
    arr2=arr2+arr[0:mid]
else:
    arr2=arr[mid+1:l]
    arr2=arr2+arr[0:mid+1]

print(arr2)
