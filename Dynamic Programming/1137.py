# N-th Tribonacci Number
class Solution:
    # Bottom-Up ; Tabulation
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
        return dp[n]
    
class Solution:
    # Top-Down ; Memoization
    def tribonacci(self, n: int) -> int:
        dp = {0:0,1:1,2:1}
        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i] = dfs(i-3) + dfs(i-2) + dfs(i-1)
            return dp[i]
        return dfs(n)




