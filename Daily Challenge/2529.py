from typing import List
class Solution:
    def lower_bound(self,nums):
        left , right = 0 , len(nums)-1
        index = len(nums)
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] <0:
                left = mid +1
            else:
                right = mid -1
                index = mid
        return index

    def upper_bound(self,nums):
        left ,right = 0 , len(nums) -1
        index = len(nums)
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] <=0:
                left = mid +1
            else:
                right = mid -1
                index = mid
        return index

    def maximumCount(self, nums: List[int]) -> int:
        positiveCount = len(nums) - self.upper_bound(nums)
        negativeCount = self.lower_bound(nums)
        return max(positiveCount,negativeCount)
    
solution = Solution()
nums = [-2,-1,-1,1,2,3]
print("Solution 1 :",solution.maximumCount(nums))