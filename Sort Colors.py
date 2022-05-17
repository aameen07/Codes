from ast import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         if not nums: return
#         n = len(nums)
#         self.quicksort(nums, 0, n-1)
#     def quicksort(self, nums, start, end):
#         if(end<=start): return
#         pivind = self.Partition(nums, start, end)
#         self.quicksort(nums, start, pivind-1)
#         self.quicksort(nums, pivind+1, end)
#     def Partition(self, nums, start, end):
#         pivot = nums[end]
#         pivind = start
#         for i in range(start, end):
#             if nums[i]<=pivot:
#                 nums[i], nums[pivind] = nums[pivind], nums[i]
#                 pivind += 1
#         nums[pivind], nums[end] = nums[end], nums[pivind]
#         return pivind
        
                # OR        
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i):
                if nums[j]>=nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]