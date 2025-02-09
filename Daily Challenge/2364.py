from typing import List

def count_bad_pairs(nums: List[int]) -> int:

    counter = {}
    bad_pairs = 0
    for i in range(len(nums)):
        diff = i - nums[i]
        good_pair = counter.get(diff, 0)
        bad_pairs += i - good_pair
        counter[diff] = good_pair + 1
    return bad_pairs

# Input
nums = [4, 1, 3, 3]

# Output
result = count_bad_pairs(nums)
print(result) 
