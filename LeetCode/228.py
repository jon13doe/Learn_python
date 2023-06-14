#228. Summary Ranges
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

#1st
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        temp = str(nums[0])

        if len(nums) == 1:
            return [temp]

        l = len(nums)
        res = []
        k = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if k > 1:
                    temp += f'->{nums[i - 1]}'
            
                res.append(temp)
                temp = str(nums[i])
                k = 1
            
            else:
                k += 1
                
        if k > 1:
            temp += f'->{nums[-1]}'
            
        res.append(temp)
    

        return res
        
#2nd
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start, end, result = 0, 0, []
        l = len(nums)
    
        while start < l and end < l:
            if end + 1 < l and nums[end] + 1 == nums[end + 1]:
                end += 1
            else:
                if start == end:
                    result.append(str(nums[start]))
                    start = start + 1
                    end = end + 1
                else:
                    result.append(str(nums[start]) + '->' + str(nums[end]))
                    start = end + 1
                    end = end + 1

        return result