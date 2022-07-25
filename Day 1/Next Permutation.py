# #         BRUTE FORCE APPROACH
# #         T.C. O(N! x N)
# #         S.C. O(A) + O(B) WHERE A->ALL PERMUTATIONS B->SET OF ALL PERMUTATIONS

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        d = sorted(nums)
        a = [list(i) for i in list(permutations(d))]
        ans = []
        for i in a:
            if i not in ans:
                ans.append(i)
                
        for i in range(len(ans)):
            if ans[i]==nums:
                
                if i==len(ans)-1:
                    for j in range(len(ans[0])):
                        nums[j] = ans[0][j]
                else:
                    for j in range(len(ans[i+1])):
                        nums[j] = ans[i+1][j]
                break
        
        
        
        
##################################################################################################
        
#         BEST OPTIMAL APPROACH
#         T.C. O(N)
#         S.C. O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        def reverse(start,end,nums):
            while start<=end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        
        i=len(nums)-2
        while i>=0 and nums[i+1]<=nums[i]:
            i-=1
        if i>=0:
            j=len(nums)-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
            
        reverse(i+1,len(nums)-1,nums)
            
            
