def sockMerchant(n, ar):
    c=0
    v=[]
    for i in ar:
        if i not in v:
            t=ar.count(i)
            if t%2!=0:
                c+=t-1
            else:
                c+=t
            v.append(i)
    return (c//2)
