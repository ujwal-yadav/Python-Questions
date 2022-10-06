class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        d= sorted(d.items(),key=lambda v:v[1],reverse=True)
        s=""
        for i,j in d:
            s+=i*j
        return s
