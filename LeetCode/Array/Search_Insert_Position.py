"""
Problem: Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/?envType=problem-list-v2&envId=array
Difficulty: Easy
Approach: use while i < len(_name of you array_) - 1 for returning position and for very last index use if else outside the loop.
Time: |Space:
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i = 0
        while i < len(nums) - 1:
            if target < nums[i]:
                return 0
            
            elif nums[i] == target:
                return i
                
            elif nums[i] < target < nums[i + 1]:
                return i + 1
                
            i = i + 1

        if target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            return len(nums)
        else:
            return len(nums) - 1
        
