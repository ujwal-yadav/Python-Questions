def generateMatrix(self, n: int) -> List[List[int]]:
   mat=[[0 for i in range(n)]for j in range(n)]
        
   t,b=0,n-1
   l,r=0,n-1
   ele=1
        
   while (t<=b and l<=r):
       for i in range(l,r):
           mat[t][i]=ele
           ele+=1
                
       for i in range(t,b):
           mat[i][r]=ele
           ele+=1
                
       for i in reversed(range(l,r+1)):
           mat[b][i]=ele
           ele+=1
                
       for i in reversed(range(t+1,b)):
           mat[i][l]=ele
           ele+=1
            
       t+=1
       b-=1
       l+=1
       r-=1
            
   return mat
   
