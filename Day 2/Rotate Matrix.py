# T.C. -> O(N^2) + O(N^2)
# S.C. -> O(N^2)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        
        temp = [[0]*n for i in range(m)]
        c = 0
        for i in matrix:
            for j in range(m):
                temp[j][n-c-1] = i[j]
            c += 1
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = temp[i][j]

###################################################################################################

# T.C. -> O(N^2) + O(N^2)
# S.C. -> O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        
        for i in range(n):
            for j in range(0,i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        def rev(a):
            i,j = 0,len(a)-1
            while i<j:
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
            return a
        for i in range(n):
            matrix[i] = rev(matrix[i])
