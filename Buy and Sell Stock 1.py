class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        s=1
        m=0
        
        while s<len(prices):
            p=prices[s]-prices[b]
            if p>0:
                m=max(p,m)
                s+=1
            else:
                b=s
                s+=1
        return m
    
