from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m =  len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and  obstacleGrid[i-1][0] == 1
            )
        for j in range(1,n):
            obstacleGrid[0][j] = int(
                obstacleGrid[0][j] == 0 and  obstacleGrid[0][j-1] == 1
            )
        for i in range(1,m):
            for j in range(1,n):
                
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = (
                        obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                    )
                else:
                     obstacleGrid[i][j] = 0 
        return obstacleGrid[m-1][n-1]


solution = Solution()
obstacleGrid1 =[[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid2 =[[0,1],[0,0]]
print("Test Case 1 : " ,solution.uniquePathsWithObstacles(obstacleGrid1))
print("Test Case 2 : " ,solution.uniquePathsWithObstacles(obstacleGrid2))