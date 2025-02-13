import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, x + 2 * y)
            operations += 1

        return operations


solution = Solution()

# Test Case 1
nums = [2,11,10,1,3]
k = 10
print(solution.minOperations(nums,k))
