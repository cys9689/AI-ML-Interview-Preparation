from typing import List


# Greedy

class Solution_:
    def maximumTripletValue(self,nums:List[int]) -> int:
        n = len(nums)
        res = 0 
        for k in range(2,n):
            maxPrefix = nums[0]
            for j in range(1,k):
                res = max(res,(maxPrefix-nums[j])*nums[k])
                maxPrefix = max(maxPrefix,nums[j])
        return res




# Greedy + Prefix
class Solution:
    def maximumTripletValue(self,nums:List[int]) -> int:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1] , nums[i-1])
            rightMax[n-i-1] = max(rightMax[n-i], nums[n-i])
        res = 0
        for j in range(1,n-1):
            res = max(res , (leftMax[j] - nums[j]) * rightMax[j])
        return res


nums = [1,10,3,4,19]
solution_ = Solution_()
print("Greedy : " , solution_.maximumTripletValue(nums))
solution = Solution()
print("Greedy + Prefix : ", solution.maximumTripletValue(nums))