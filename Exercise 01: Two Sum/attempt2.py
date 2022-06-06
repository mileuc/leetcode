class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution_indices = [] # Solution output
        for first_num_index in range(len(nums) - 1):    # For the index of the first addition term from 0 to the Length of nums - 1...
            second_num_index = len(nums) - 1     # Have the index of the second addition term start from the last number in nums
            while second_num_index > first_num_index:   # While the index of the second addition term is greater than the index of the first addition term
                sum_num = nums[first_num_index] + nums[second_num_index]    # Sum the two numbers and see if it matches the target
                if sum_num == target:   # If sum matches target, add their indices to the solution output
                    solution_indices.append(first_num_index)    
                    solution_indices.append(second_num_index)
                    return solution_indices
                else:   # If sum doesn't match target, subtract the index of the second number by 1
                    second_num_index -= 1 
