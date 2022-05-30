class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        inv=sorted(intervals)
        merged=[[inv[0][0],inv[0][1]]]
        
        for i in range(1,len(inv)):
            if inv[i][0]<=merged[-1][1]:
                merged[-1][1]=max(merged[-1][1],inv[i][1])
            else:
                merged.append([inv[i][0],inv[i][1]])
        return merged
