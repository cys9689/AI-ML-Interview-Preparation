class Solution:
    def clearDigits(self, s: str) -> str:
        result = []  
        for char in s:
            if char.isdigit():
                if result: 
                    result.pop() 
            else:
                result.append(char) 
        return "".join(result) 
    

# Test cases
solution = Solution()
s1 = 'abc'
s2 = "cb34"
print("Case 1 Output:", solution.solution.clearDigits(s1))  # Expected output: "abc"
print("Case 2 Output:", solution.solution.clearDigits(s2))  # Expected output: ""

