def trap(self, height: List[int]) -> int:
        left=[]
        right=[-1]*(len(height)-1)
        left.append(height[0])
        right.append(height[len(height)-1])
        i=1
        j=len(height)-2
        count=0
        while i<len(height) and j>=0:
            left.append(max(height[i],left[i-1]))
            right[j]=max(height[j],right[j+1])
            i+=1
            j-=1
        
        for i in range(len(height)):
            count+=min(left[i],right[i])-height[i]
        
        return count      
