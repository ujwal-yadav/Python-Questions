def maxSubArraySum(self,arr,N):
        sum=0
        max=arr[0]
        for i in range(len(arr)):
            sum+=arr[i]
            if sum>max:
                max=sum
            if sum<0:
                sum=0
        return max
