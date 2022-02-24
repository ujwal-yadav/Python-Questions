num=[1,2]
lst=[]
lsst=list()
for i in range(len(num)):
    nums=num[i:]+num[:i]
    for j in range(len(nums)+1):
            lst.append(nums[:j])
lst=list(filter(None,lst))
print(lst)
