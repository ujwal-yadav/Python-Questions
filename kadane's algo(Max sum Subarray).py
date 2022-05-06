def maxSubArray(self, nums: List[int]) -> int:
    summ=0
    c=0
    temp=[]
    maxx=nums[0]
    for i in range(len(nums)):
        summ+=nums[i]
        if summ>maxx:
            temp=[]
            maxx=summ
            temp.append(c)
            temp.append(i)
        if summ<0:
            summ=0
            c=i+1
    if len(temp)<1:
            print(nums[0])
        else:
            for i in range(temp[0],temp[1]+1):
                print(nums[i],end=" ")
    return maxx
                
