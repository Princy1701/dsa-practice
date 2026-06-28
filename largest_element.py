'''problem statement: 
Given an array of integers nums, return the value of the largest element in the array

Example 1
Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6

Example 2
Input: nums = [3, 3, 0, 99, -40]
Output: 99
Explanation: The largest element in array is 99 '''

#solution:
#largest element with brute force or simple logic on day-1 of solving dsa problems

class Solution:
    def largestElement(self, nums):
        largest=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>largest:
                largest=nums[i]
        return largest
        