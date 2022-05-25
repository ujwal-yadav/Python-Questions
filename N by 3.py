class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        temp=[]
        for i in nums:
            if i not in temp:
                if nums.count(i)>len(nums)//3:
                    temp.append(i)
        return temp
                    
