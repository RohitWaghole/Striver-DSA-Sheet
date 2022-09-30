class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums)//2
        for i in nums:
            if nums.count(i)>major:
                return i

###################################################################################

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

##################################################################################

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        for key,val in d.items():
            if val>(len(nums)//2):
                return key

###################################################################################

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        element = None
        
        for i in nums:
            if cnt == 0:
                element = i
            if element == i:
                cnt += 1
            else:
                cnt -= 1
        return element
