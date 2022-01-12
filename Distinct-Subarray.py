array=[1,2,3];
import itertools 
 
print(array)
comb = [array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
 
print(comb)
c=0
for i in comb:
    if sum(i)%2!=0:
        c+=1;
print("Total no of comb are ",c)
