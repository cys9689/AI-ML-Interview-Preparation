from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        freq_ = {}
        result = 0 
        
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                if product in freq_:
                    freq_[product] += 1
                else:
                    freq_[product] = 1
        
        for product_freq in freq_.values():
            pair_of_equal_product = ((product_freq - 1) * product_freq // 2)
            result += pair_of_equal_product * 8
        
        return result
