from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0 
        zero_count = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
        print(zero_count)
        nums = [i for i in nums if i!= 0]
                
        return nums + zero_count *[0]
    
solution = Solution()
nums = [1,2,2,1,1,0]
print(solution.applyOperations(nums))