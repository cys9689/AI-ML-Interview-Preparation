
class Solution:
    def remove_occurrences(self, s: str, part: str) -> str:

        stack = []
        part_length = len(part)

        for char in s:
            stack.append(char)
            if len(stack) >= part_length and self._matches(stack, part, part_length):
                # Remove the matched substring
                for _ in range(part_length):
                    stack.pop()

        return "".join(stack)

    def _matches(self, stack: list[str], part: str, part_length: int) -> bool:
        return "".join(stack[-part_length:]) == part




# Test cases
solution = Solution()

s1 = "daabcbaabcbc"
part1 = "abc"
print("Case 1 Output:", solution.remove_occurrences(s1, part1)) # Expected output: "dad"



s2 = "axxxxyyyyb"
part2 = "xy"
print("Case 2 Output:", solution.remove_occurrences(s2, part2))  # Expected output: "ab"

