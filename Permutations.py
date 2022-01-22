import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        comb=list(itertools.permutations(nums,len(nums)))
        return(comb)
