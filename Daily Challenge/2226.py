from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0 

        left, right = 1, max(candies) 

        while left <= right:
            middle = left + (right - left) // 2
            if self.can_allocate(candies, k, middle):
                left = middle + 1
            else:
                right = middle - 1
                
        return right  

    def can_allocate(self, candies: List[int], k: int, num_of_candies: int) -> bool:
        if num_of_candies == 0: 
            return False

        max_num_of_children = sum(candy // num_of_candies for candy in candies)
        return max_num_of_children >= k

solution = Solution()
print("Test Case 1 : ",solution.maximumCandies([5,8,6] , k = 3))
print("Test Case 2 : ",solution.maximumCandies([2,5] , k = 11))
