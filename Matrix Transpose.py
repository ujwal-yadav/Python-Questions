c = [[12,7],
    [4 ,5],
    [3 ,8]]
    
result = [[0,0,0],
         [0,0,0]]

for i in range(len(mat)):
   for j in range(len(mat[0])):
       result[j][i] = mat[i][j]

for r in result:
   print(r)
