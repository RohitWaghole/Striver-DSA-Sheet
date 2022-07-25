# T.C. -> O(N x M + (N + M))
# S.C. -> O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:

                    row = i
                    col = j
                    for m in range(len(matrix[0])):
                        if matrix[row][m]!=0: matrix[row][m] = 'a'
                    for m in range(len(matrix)):
                        if matrix[m][col]!=0: matrix[m][col] = 'a'
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='a':
                    matrix[i][j] = 0

##########################################################################################################

# T.C. -> O(N x M)
# S.C. -> O(N + M)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        r = ['a']*len(matrix)
        c = ['a']*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    r[i]=0
                    c[j]=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if r[i]==0 or c[j]==0:
                    matrix[i][j] = 0

##########################################################################################################

# T.C. -> 2 x O(N x M)
# S.C. -> O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col0 = 1
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][0]==0: col0=0
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(row-1,-1,-1):
            for j in range(col-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
            if col0==0: matrix[i][0] = 0
