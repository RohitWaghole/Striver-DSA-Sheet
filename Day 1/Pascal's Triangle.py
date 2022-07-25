# T.C. -> ~O(N^2)
# S.C. -> O(N)

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        
        pascal = [[1]]
        for i in range(n-1):
            temp = [1]
            for j in range(len(pascal[-1])-1):
                temp.append(pascal[-1][j]+pascal[-1][j+1])
            temp.append(1)
            pascal.append(temp)
        return pascal
