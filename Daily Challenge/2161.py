from typing import List
from collections import deque

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        q = deque()
        pivot_ = 0
        result = []
        for num in nums:
            if num < pivot:
                result.append(num)
            elif num == pivot:
                pivot_ += 1
            else:
                q.append(num)
        while pivot_> 0 :
            result.append(pivot)
            pivot_ -=1
        while q:
            element = q.popleft()
            result.append(element)
        return result


solution = Solution()
nums = [9,12,5,10,14,3,10]
pivot = 10
print(solution.pivotArray(nums,pivot))