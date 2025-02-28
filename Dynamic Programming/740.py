from functools import cache
from collections import defaultdict
from typing import List

class Solution:
    def deleteAndEarn(self,nums:List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number,num)
        @cache
        def max_points(num):
            if num == 0:
                return 0 
            if num ==1:
                return points[1]
            return max(max_points(num-1),max_points(num-2)+points[num])
        

solution = Solution()
num1 = [2,2,3,3,3,4]
print(solution.deleteAndEarn(num1))