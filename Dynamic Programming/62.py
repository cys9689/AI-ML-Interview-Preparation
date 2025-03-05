class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]
        for col in range(1,m):
            for row in range(1,n):
                d[col][row] = d[col-1][row] + d[col][row-1]
        return d[m-1][n-1]
    

solution = Solution()
print("Test Case 1 ( m =3 ,n = 7) : " , solution.uniquePaths(3,7))
print("Test Case 2 ( m =3 ,n = 2) : " , solution.uniquePaths(3,2))
