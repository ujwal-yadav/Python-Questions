def mergeSort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    mergeSort(left)
    mergeSort(right)

    merge(left, right, arr)

def merge(a,b,arr):
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len(a):
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len(b):
        arr[k] = b[j]
        j+=1
        k+=1

arr=[12,30,20,5,18]
mergeSort(arr)
print("Sorted Array:",arr)
