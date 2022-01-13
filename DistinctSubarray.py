import itertools;
arr=[1,2,3,4];

j=3;
comb=[arr[i:j+1] for i in range(len(arr)) for j in range(i,len(arr))]
print(comb);

s=0
for i in comb:
    if sum(i)%2!=0:
        s+=1;
print("No of Subarrays are : ",s)
