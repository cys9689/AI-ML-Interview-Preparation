# Leetcode 1524 
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)
        for i in range(n):
            arr[i] %= 2
        dp_even,dp_odd = [0] * n ,[0] *n

        if arr[n-1] == 0:
            dp_even[n-1] = 1
        else:
            dp_odd[n-1] = 1
        
        for num in range(n-2,-1,-1):
            if arr[num] == 1:
                dp_odd[num] = (1+dp_even[num+1]) %MOD
                dp_even[num] = dp_odd[num+1]
            else:
                dp_even[num] = (1 + dp_even[num + 1]) % MOD
                dp_odd[num] = dp_odd[num+1]

        count = 0 
        for odd_count in dp_odd:
            count += odd_count
            count %= MOD
        return int(count)



# Input 1
solution = Solution() 
arr1 =[1,3,5]
print("output 1 : " , solution.numOfSubarrays(arr1))