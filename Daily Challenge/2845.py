from typing import List
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        count = {0:1}
        current_prefix_count = 0
        result = 0 
        for i in range(n):
            if nums[i] % modulo == k:
                current_prefix_count += 1
            current_mod = current_prefix_count % modulo
            target_mod = (current_mod -k + modulo) % modulo
            result += count.get(target_mod,0)
            count[current_mod]= 1+count.get(current_mod,0)
        return result

solution = Solution()
nums = [3,2,4]
modulo = 2 
k =1
print('solution 1 ',solution.countInterestingSubarrays(nums,modulo,k))