class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        x = s.split(' ')
        lp = len(set(p))
        lx = len(set(x))

        if len(p)!=len(x) or lp!=lx:
            return False
        
        if lp == len(set(zip(p, x))):
            return True
    
                
