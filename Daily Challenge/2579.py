class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n*(n-1)*2
    

solution = Solution()
print("Result 1 : n =1 ", solution.coloredCells(1))
print("Result 2 : n =2 ", solution.coloredCells(2))
