nums=[1,2,3,4]
answer=[]
t=1
for i in range(len(nums)):
  answer.append(t)
  t=t*nums[i]
t=1
for i in range(len(nums)-1,-1,-1):
  answer[i]=answer[i]*t
  t=t*nums[i]
print(answer)
