class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp=[]
        lst=sorted(score, reverse=True)
        
        for i in score:
            index=lst.index(i)
            if index+1==1:
                temp.append("Gold Medal")
            elif index+1==2:
                temp.append("Silver Medal")
            elif index+1==3:
                temp.append("Bronze Medal")
            else:
                temp.append(str(index+1))
        return temp
