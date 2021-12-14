import itertools

arr=[2,3,5,0,4,1];
comb=list(itertools.combinations(arr,2))
c=0;
for i in comb:
    i=sum(i);
    if (i==5):
        c+=1;
print(c);
