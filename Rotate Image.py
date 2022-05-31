class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        result = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
        
        for i in range(len(matrix)-1,-1,-1):
            temp=matrix[len(matrix)-1-i]
            for j in range(len(matrix[0])):
                result[j][i]=temp[j]
                
        for i in range(len(result)):
            matrix[i]=result[i] 
