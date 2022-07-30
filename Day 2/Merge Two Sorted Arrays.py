class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        l = []
        for i in range(m):
            l.append(nums1[i])
        for i in range(n):
            l.append(nums2[i])
        l.sort()
        for i in range(m+n):
            nums1[i] = l[i]

###############################################################################################

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()

###############################################################################################

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        while m and n:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n:
            nums1[:n] = nums2[:n]
