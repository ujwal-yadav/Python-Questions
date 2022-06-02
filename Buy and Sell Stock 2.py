class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        s=1
        p=0
        while s<len(prices):
            if prices[b]>prices[s]:
                b=s
                s+=1
            else:
                p+=prices[s]-prices[b]
                b+=1
                s+=1
        return p
