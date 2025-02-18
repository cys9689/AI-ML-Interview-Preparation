from itertools import permutations

class Solution1:
    def smallestNumber(self, pattern: str) -> str:
        numbers = list(range(1, 10))  
        limit = len(pattern) + 1
        result = float("inf")
        combinations = ["".join(map(str, p)) for p in permutations(numbers, limit)]
        for i in combinations:
            if self.validate(pattern,i):
                result = min(result,int(i))

        return str(result)
    def validate(self,pattern,test):
        for i in range(1,len(test)):
            if pattern[i-1] == "I":
                if test[i] > test[i-1]:
                    continue
                else:
                    return False
            if pattern[i-1] == "D":
                if test[i] < test[i-1]:
                    continue
                else:
                    return False
        return True

# Solution 1 -> Brute Force -> TLE


class Solution2:
        def smallestNumber(self, pattern: str) -> str:
            result = []
            num_stack = []
            for index in range(len(pattern)+1):
                num_stack.append(index+1)
                if index == len(pattern) or pattern[index] == "I":
                    while num_stack:
                        result.append(str(num_stack.pop()))
            return "".join(result)
        
solution = Solution2()
pattern = "IIIDIDDD"
print(solution.smallestNumber(pattern))
