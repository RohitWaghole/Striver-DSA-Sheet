class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        major = len(nums)//3
        res = []
        
        for i in set(nums):
            if nums.count(i)>major:
                res.append(i)
                
        return res
    
############################################################################################

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums)//3
        
        d = Counter(nums)
        result = []
        
        for key,val in d.items():
            if val>majority:
                result.append(key)
        
        return result

################################################################################################

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        c1,c2 = 0,0
        n1,n2 = None,None
        
        for i in nums:
            if i==n1:
                c1 += 1
            elif i==n2:
                c2 += 1
            elif c1 == 0:
                n1 = i
                c1 = 1
            elif c2==0:
                n2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        major = len(nums)//3
        a = nums.count(n1)
        b = nums.count(n2)
        
        res = []
        if a>major:
            res.append(n1)
        if b>major:
            res.append(n2)
        return res
    
    
    
