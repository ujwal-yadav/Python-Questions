def appleAndCoupon(n: int, m : int, arr: List[int])-> int:
    arr=sorted(arr,reverse=True)
    s=0
    t=arr[:m]
    t=t[len(t)-1]
    c=False
    for i in arr:
        if i==t and c==False:
            c=True
            continue
        else:
            s+=i
    return s
