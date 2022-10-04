class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        totalPairs = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] > 2*nums[j]:
                    totalPairs += 1
        return totalPairs
    
###########################################################################################################

class Solution:
    
    def merge(self, nums, low, mid, high):
        
        count = 0
        j = mid + 1
        for i in range(low, mid+1):
            while j<=high and nums[i] > 2*nums[j]:
                j += 1
            count += j - (mid + 1)
            
        temp = []
        left = low
        right = mid + 1
        while left <= mid and right<=high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
            
        for i in range(low, high+1):
            nums[i] = temp[i-low]
            
        return count
    
    def mergeSort(self, nums, low, high):
        if low >= high:
            return 0
        mid = low + (high - low)//2
        inv = self.mergeSort(nums, low, mid)
        inv += self.mergeSort(nums, mid + 1, high)
        inv += self.merge(nums, low, mid, high)
        return inv
    
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums)-1)
    
    
    
    
    
    
    
    
