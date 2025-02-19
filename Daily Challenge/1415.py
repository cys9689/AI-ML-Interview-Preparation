# Backtrack Recursion Approach 

class Solution1:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ["a","b","c"]
        result = []
        def generate(current_string):
            if len(current_string) == n:
                result.append(current_string)
                return
            for l in letters:
                if not current_string or current_string[-1] != l:
                    generate(current_string + l)
        generate("")
        result.sort()
        return result[k-1]  if k<= len(result) else ""
       

solution1 = Solution1()
n1 = 3
k1 = 9
print(solution1.getHappyString(n1,k1))


class Solution2:
    def getHappyString(self,n:int,k:int) -> str:
        strings_stack = []
        index_in_sorted_list = 0
        strings_stack.append("")
        while strings_stack:
            current_string = strings_stack.pop()
            if len(current_string) == n:
                index_in_sorted_list += 1
                if index_in_sorted_list == k:
                    return current_string
                continue
            for current_char in reversed(["a","b","c"]):
                if (len(current_string) == 0 or current_string[-1] != current_char):
                    strings_stack.append(current_string + current_char)
        return ""


solution2 = Solution2()
n2 = 3
k2 = 9
print(solution2.getHappyString(n2,k2))
