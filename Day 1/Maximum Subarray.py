class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx, s = nums[0],0
        for i in range(len(nums)):
            s += nums[i]
            mx = max(mx,s)
            if s<0:
                s = 0
        return mx
    
#################################################################################

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx,mn = nums[0],nums[0]
        for i in range(1,len(nums)):
            mn = max(nums[i],nums[i] + mn)
            mx = max(mx, mn)
        return mx

####################################################################################

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)):
            if nums[i-1]>=0:
                nums[i]+=nums[i-1]
        return max(nums)
