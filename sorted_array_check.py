'''Problem statement      
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

Example 1
Input : nums = [1, 2, 3, 4, 5]
Output : true
Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

Example 2
Input : nums = [1, 2, 1, 4, 5]
Output : false
Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false
'''

#solution 
#approach 1:brute force

class Solution:
    def isSorted(self, nums):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        return True