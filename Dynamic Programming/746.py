# 746 Min Cost Climbing Stairs
from typing import List
class Solution:
    def minCostClimbingStairs(self,cost:List[int]) -> int:
        dp = [0] * (len(cost) + 1 )
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
        return dp[-1]
    


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i-1] + dfs(i-1), cost[i-2] + dfs(i-2))
            return memo[i]
        return dfs(len(cost))
    

solution1 = Solution()
cost = [10,15,20]
solution2 = Solution2()

print(solution1.minCostClimbingStairs(cost))
print(solution2.minCostClimbingStairs(cost))