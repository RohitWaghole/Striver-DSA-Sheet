# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         nums.sort()

#########################################################################################################

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         zero,one,two = 0,0,0
#         for i in nums:
#             if i==0:
#                 zero+=1
#             elif i==1:
#                 one+=1
#             else:
#                 two+=1
#         i=0
#         while zero:
#             nums[i]=0
#             i+=1
#             zero-=1
#         while one:
#             nums[i]=1
#             i+=1
#             one-=1
#         while two:
#             nums[i]=2
#             i+=1
#             two-=1

#########################################################################################################

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start,mid,end = 0,0,len(nums)-1
        while mid<=end:
            if nums[mid]==0:
                nums[start],nums[mid]=nums[mid],nums[start]
                start+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[end]=nums[end],nums[mid]
                end-=1
