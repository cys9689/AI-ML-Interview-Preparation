from typing import List
import heapq

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map = {}

        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            digit_sum_map.setdefault(digit_sum, []).append(num)

        max_sum = -1
        for values in digit_sum_map.values():
            if len(values) > 1:
                values.sort()
                max_sum = max(max_sum, sum(values[-2:]))

        return max_sum



solution = Solution()

#Test Case 1 
nums1= [18,43,36,13,7]
print(solution.maximumSum(nums1))




# Solution 2 



class Solution2:
    def calculate_digit_sum(self, num: int) -> int:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map = [[] for _ in range(82)]
        max_sum = -1

        for num in nums:
            digit_sum = self.calculate_digit_sum(num)
            heapq.heappush(digit_sum_map[digit_sum], num)

            if len(digit_sum_map[digit_sum]) > 2:
                heapq.heappop(digit_sum_map[digit_sum])

        for values in digit_sum_map:
            if len(values) == 2:
                max_sum = max(max_sum, sum(values))

        return max_sum


solution2 = Solution2()

#Test Case 1 
nums1= [18,43,36,13,7]
print(solution2.maximumSum(nums1))

