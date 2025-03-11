from typing import List
#Bottom-up (Iterative) : Inplace

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1,len(triangle)):
            for col in range(row+1):
                smallest_above = float('inf')
                if col >0:
                    smallest_above = triangle[row-1][col-1]
                if col<row:
                    smallest_above = min(smallest_above,triangle[row-1][col])
                triangle[row][col] += smallest_above
        return min(triangle[-1])

#Bottom-up(Iterative) - Auxilliary Space
class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[0]
        for row in range(1,len(triangle)):
            current_row = []
            for col in range(row+1):
                smallest_above = float('inf')
                if col >0:
                    smallest_above = prev_row[col-1]
                if col<row:
                    smallest_above = min(smallest_above,prev_row[col])
                current_row.append(triangle[row][col] + smallest_above)
            prev_row = current_row
        return min(prev_row)

triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]

solution1 = Solution1()
print(solution1.minimumTotal(triangle1))

solution = Solution()
print(solution.minimumTotal(triangle1))