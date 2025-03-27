from typing import List
from collections import defaultdict

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        first_map = defaultdict(int)
        second_map = defaultdict(int)
        n = len(nums)
        for num in nums:
            second_map[num] += 1 
        for index in range(n):
            num = nums[index]
            second_map[num] -=1
            first_map[num] +=1
            if (
                first_map[num] *2 > index+1
                and 
                second_map[num] *2 >n-index-1):
                return index
        return -1

nums1 = [1,2,2,2]
nums2 = [2,1,3,1,1,1,7,1,2,1]
solution = Solution()
print("Test Case 1:" , solution.minimumIndex(nums1))
print("Test Case 2:" , solution.minimumIndex(nums2))