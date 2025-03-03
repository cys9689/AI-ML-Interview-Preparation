from typing import List

# Hashmap
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result  = {}
        for key,value in nums1:
            if key in result:
                result[key] += value
            else:
                result[key] = value
        for key, value in nums2:
            if key in result:
                result[key] += value
            else:
                result[key] = value 
        sorted_items = sorted(result.items())
        return sorted_items
    
# Two pointer
class Solution2:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mergedArray = []
        i,j = 0,0    
        while i< len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                temp_sum = nums1[i][1]+ nums2[j][1]
                mergedArray.append((nums1[i][0],temp_sum))
                i +=1
                j+=1
            elif nums1[i][0] < nums2[j][0]:
                mergedArray.append((nums1[i][0],nums1[i][1]))
                i+=1
            else:
                mergedArray.append((nums2[j][0],nums2[j][1]))
                j+=1
        while i < len(nums1):
            mergedArray.append(nums1[i])
            i+=1
        while j < len(nums2):
            mergedArray.append(nums2[j])
            j+=1
        return mergedArray



solution = Solution()
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(solution.mergeArrays(nums1,nums2))


solution2 = Solution2()
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(solution2.mergeArrays(nums1,nums2))