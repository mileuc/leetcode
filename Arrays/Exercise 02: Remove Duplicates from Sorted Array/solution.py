"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Assign initial value of unique_numbers to be 1 (first value auto-included)
        unique_numbers = 1

        # Change nums array so that the first k elements of nums contain unique elements
        for i in range(1, len(nums)):
            # If array value does not match previous value... (new unique value found)
            if nums[i] != nums[i - 1]:
                nums[unique_numbers] = nums[i] # Replace value after the last unique number with current value
                unique_numbers = unique_numbers + 1 # Increment unique_numbers

        # Return unique numbers
        return unique_numbers
