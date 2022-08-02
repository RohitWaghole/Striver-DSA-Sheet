'''
Time Complexity: O(NlogN)+O(N*N). O(NlogN) for sorting the array, and O(N*N) because we are checking to the right for each index which is a nested loop.

Space Complexity: O(N), as we are using a separate data structure.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        ans = []
        
        for i in range(len(intervals)):
            
            start,end = intervals[i]
            
            if ans!=[]:
                
                if start<= ans[-1][1]:
                    continue
            
            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
            
            end = max(end, intervals[i][1])
            ans.append([start, end])
            
        return ans
    
#########################################################################################################

'''
Time Complexity: O(NlogN) + O(N). O(NlogN) for sorting and O(N) for traversing through the array.

Space Complexity: O(N) to return the answer of the merged intervals.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        intervals.sort()
        res = []
        a = intervals[0]
        
        for i in range(1,len(intervals)):
            b = intervals[i]
            
            if a[1]>=b[0]:
                a[1] = max(a[1],b[1])
            else:
                res.append(a)
                a = intervals[i]
        res.append(a)
        return res
 
