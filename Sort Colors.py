class Solution:
    def sortColors(self, nums: List[int]) -> None:
        temp=[]
        for i in range(3):
            for j in range(len(nums)):
                if nums[j]==i:
                    temp.append(nums[j])
                    
        for i in range(len(nums)):
            nums[i]=temp[i]
