def makeQualityArray(a: List[int]) -> int:
    c=0
    for i in a:
        e,o=False,False
        for j in range(2, i + 1):
            if i % j == 0:
                if j%2==0:
                    e=True
                else:
                    o=True
            if e and o:
                break
        if not e or not o:
            c+=1
    return c
