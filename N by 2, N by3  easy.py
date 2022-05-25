class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=len(nums)//2
        temp=[]
        for i in nums:
            c=0
            if i not in temp:
                for j in nums:
                    if i==j:
                        c+=1
            temp.append(i)
            if c>s:
                return i
