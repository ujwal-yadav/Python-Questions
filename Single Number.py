class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr=[0]*len(nums)
        for i in range(len(nums)):
            arr[i]=nums.count(nums[i])
            if arr[i]==1:
                return nums[i]
