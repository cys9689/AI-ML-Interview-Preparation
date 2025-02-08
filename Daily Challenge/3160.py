from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = []
        color_map = {}  
        ball_map = {}  

        for ball, color in queries:
            if ball in ball_map:
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1
                if color_map[prev_color] == 0:
                    del color_map[prev_color]

            ball_map[ball] = color
            color_map[color] = color_map.get(color, 0) + 1
            result.append(len(color_map))

        return result

# Test cases
solution = Solution()


limit1 = 4
queries1 = [[1, 4], [2, 5], [1, 3], [3, 4]]
print("Case 1 Output:", solution.queryResults(limit1, queries1))  # Expected output: [1, 2, 2, 3]


limit2 = 4
queries2 = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
print("Case 2 Output:", solution.queryResults(limit2, queries2))  # Expected output: [1, 2, 2, 3, 4]
