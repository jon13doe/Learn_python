#189. Rotate Array
#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#1st
class Solution:
    def rotate(self, nums, k):
        l = len(nums)
        if k == 0 or l == 1:
            return nums

        if k > l:
            k -= (k // l) * l

        nums[: k], nums[k:] = nums[-k:], nums[:-k]
        
#2nd
class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]
    