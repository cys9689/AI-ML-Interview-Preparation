from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        result = 0 
        alternating_elements_count = 1
        last_color = colors[0]
        for index in range(1,n):
            if colors[index] == last_color:
                alternating_elements_count = 1
                last_color = colors[index]
                continue
            alternating_elements_count += 1
            if alternating_elements_count >=k:
                result +=1
            last_color = colors[index]
        for index in range(k-1):
            if colors[index] == last_color:
                break
            alternating_elements_count +=1
            if alternating_elements_count >= k:
                result +=1
            last_color = colors[index]
        return result
    
class Solution1:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k-1):
            colors.append(colors[i])
        length = len(colors)
        result = 0 
        left ,right = 0,1
        while right < length:
            if colors[right] == colors[right-1]:
                left = right
                right +=1
                continue
            
            right +=1
            if right - left <k:
                continue
            result +=1
            left += 1
        return result
        

solution = Solution()
colors = [0,1,0,1,0]
k = 3
print("solution 1:" , solution.numberOfAlternatingGroups(colors,k))
solution1 = Solution()
print("solution 2:" , solution1.numberOfAlternatingGroups(colors,k))
