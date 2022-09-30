class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False

    
####################################################################################

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==target:
                    return True
        return False

####################################################################################

class Solution:
    def binarysearch(self,a,target):
        n = len(a)
        lo,hi = 0,n-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if a[mid]==target:
                return True
            if a[mid]<target:
                lo=mid+1
            else:
                hi=mid-1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        for i in matrix:
            if i[0]<=target<=i[-1]:
                if self.binarysearch(i,target):
                    return True
        return False
