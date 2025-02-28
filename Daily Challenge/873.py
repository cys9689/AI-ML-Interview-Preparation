from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        max_len = 0 
        dp = [[0] * n for _ in range(n)]
        val_to_idx = {num : idx for idx,num in enumerate(arr)}
        for curr in range(n):
            for prev in range(curr):
                diff = arr[curr] - arr[prev]
                prev_idx = val_to_idx.get(diff,-1)
                dp[prev][curr] = (
                    dp[prev_idx][prev] + 1 
                    if diff < arr[prev] and prev_idx >= 0
                    else 2
                )
                max_len = max(max_len,dp[prev][curr])
        print(dp)
        return max_len if max_len > 2  else 0 
    

solution = Solution()
arr1 = [1,2,3,4,5,6,7,8]
print(solution.lenLongestFibSubseq(arr1))