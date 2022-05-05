def generate(self, numRows: int) -> List[List[int]]:
    mat=[[1]]
    n=numRows
    
    for i in range(1,n):
        temp=[1]
        for j in range(0,i):
            if i>1 and j<i-1:
                s=mat[i-1][j]+mat[i-1][j+1]
                temp.append(s)
        temp.append(1)
        mat.append(temp)
    return mat
