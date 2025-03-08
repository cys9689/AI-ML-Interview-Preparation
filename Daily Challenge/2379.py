from collections import deque

# Solution : Sliding Windows
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        num_whites = 0
        num_recolors = float("inf")
        for right in range(len(blocks)):
            if blocks[right] == "W":
                num_whites += 1 
            if right -left + 1 == k:
                num_recolors = min(num_recolors,num_whites)

                if blocks[left] == "W":
                    num_whites -= 1
                
                left += 1
        return num_recolors


# Solution : Queues
class Solution1:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        queue = deque()
        num_whites = 0 
        for i in range(k):
            current_char = blocks[i]
            if current_char == "W":
                num_whites += 1
            queue.append(current_char)
        num_recolors = num_whites

        for i in range(k,len(blocks)):
            if queue.popleft() == "W":
                num_whites -=1
            current_char = blocks[i]
            if current_char == "W":
                num_whites +=1
            queue.append(current_char)

            num_recolors = min(num_recolors,num_whites)
        return num_recolors
    
blocks = "WBWBBBW"
k=2
solution = Solution()
print("Test Case 1:" , solution.minimumRecolors(blocks,k))
solution1 = Solution1()
print("Test Case 1:" ,solution1.minimumRecolors(blocks,k))
