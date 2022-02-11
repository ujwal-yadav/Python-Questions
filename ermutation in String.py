class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s2 and not s1:
            return True
        s1 = "".join(sorted(list(s1)))
        k = len(s1)
        
        for i in range(len(s2)):
            sub = s2[i:i+k]
            sub_str = "".join(sorted(list(sub)))
            
            if s1 == sub_str:
                return True
        return False
