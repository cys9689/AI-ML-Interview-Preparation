
# Brute Force Solution -> TLE
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        result = 0
        for i in range(start,finish+1):
            ele = str(i)
            n = len(s)
            if ele.endswith(s) and all(int(d) <= limit for d in ele):
                result +=1
        return result


