from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        my_dict = {key: 0 for key in range(1,m*n+1)}
        for i in range(m):
            for j in range(n):
                my_dict[grid[i][j]] +=1
        repeat,missing =0,0
        for key,val in my_dict.items():
            if val > 1:
                repeat = key
            if val ==0 :
                missing = key
        return [repeat,missing]

solution = Solution()
grid1 = [[1,3],[2,2]]
print(solution.findMissingAndRepeatedValues(grid1))