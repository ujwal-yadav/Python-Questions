mat=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

arr1=[-1 for i in range(len(mat))]
arr2=[-1 for i in range(len(mat[0]))]

for i in range(len(mat)):
    for j in  range(len(mat[0])):
        if mat[i][j]==0:
            arr1[i]=0
            arr2[j]=0

for i in range(len(mat)):
    for j in  range(len(mat[0])):
        if arr1[i]==0 or arr2[j]==0:
            mat[i][j]=0
print(mat)
