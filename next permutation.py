class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        i,j=0,0
        for i in range(n-2,-2,-1):
            if nums[i]<nums[i+1]:
                break
        if i<0:
            temp=nums[::-1]
            for v in range(0,n):
                nums[v]=temp[v]
                
        else:
            for j in range(n-1,i,-1):
                if nums[j]>nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                    temp=nums[n-1:i:-1]
                    new=nums[0:i+1]+temp
                    for t in range(0,n):
                        nums[t]=new[t]
                    break
