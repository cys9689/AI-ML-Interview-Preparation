class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 0 
        while 3 ** power <= n:
            power +=1
        while n > 0:
            if n >= 3**power:
                n-= 3**power
            if n>= 3**power:
                return False
            power -= 1 
        return True


solution = Solution()
print("Test Case 1 (n=12):" , solution.checkPowersOfThree(12))
print("Test Case 2 (n=91):" , solution.checkPowersOfThree(91))
print("Test Case 3 (n=21):" , solution.checkPowersOfThree(21))
