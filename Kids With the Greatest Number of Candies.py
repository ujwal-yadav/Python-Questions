class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        temp=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m:
                temp.append(True)
            else:
                temp.append(False)
        return temp
