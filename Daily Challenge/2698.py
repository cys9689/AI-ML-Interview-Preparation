class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishmentNum = 0
        for i in range(1,n+1):
            square_num = i * i 
            string_num = str(square_num)
            memo_array = [
                [-1] * (i+1) for _ in range(len(string_num))
            ]
            if self.findPartitions(0,0,string_num,i,memo_array):
                punishmentNum += square_num
        return punishmentNum
    
    def findPartitions(self, start_index,current_sum,string_num,target,memo):
        if start_index == len(string_num):
            return current_sum == target
        if current_sum > target:
            return False
        if memo[start_index][current_sum] != -1:
            return memo[start_index][current_sum] == 1
        
        partition_found = False
        for current_index in range(start_index,len(string_num)):
            current_string = string_num[start_index: current_index +1]
            addend = int(current_string)
            partition_found = partition_found or self.findPartitions(
                current_index+1,
                current_sum + addend,
                string_num,
                target,
                memo
            )
            if partition_found:
                memo[start_index][current_sum] = 1
                return True
        memo[start_index][current_sum] =0
        return False



solution = Solution()
# Case 1 
n1 = 10
print(solution.punishmentNumber(10))
