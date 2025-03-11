from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for row in range(1,n):
            for col in range(n):
                if col == 0 :
                    smallest_above = min(matrix[row-1][col],matrix[row-1][col+1])
                elif col == n - 1:
                    smallest_above = min(matrix[row-1][col],matrix[row-1][col-1])
                else:
                    smallest_above = min(matrix[row-1][col-1],matrix[row-1][col],matrix[row-1][col+1])
                matrix[row][col] += smallest_above
        return min(matrix[-1])

solution = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
print('solution 1: ', solution.minFallingPathSum(matrix))