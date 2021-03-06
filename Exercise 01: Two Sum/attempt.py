class Solution:
    """
    self represents the instance of the class, and Self is always pointing to Current Object.
    by using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:    # has to return a list of integers
        solution_indices = []
        # iterate through each number in the list and add it to each number that comes after it (starting with the last number in the list)
        for first_number_index in range(len(nums) - 1):
            second_number_index = len(nums) - 1     # reset second index to equal the last index each time
            while second_number_index > first_number_index:     # while the second index is greater than the first, add their values and if it equals the target
                sum_value = nums[first_number_index] + nums[second_number_index]
                if sum_value == target:
                    solution_indices.append(first_number_index)
                    solution_indices.append(second_number_index)
                    return solution_indices
                else:
                    second_number_index -= 1
                          
# two_sum_finder = Solution()
# output = two_sum_finder.twoSum([2, 7, 11, 15], 9)
# print(output)

# two_sum_finder = Solution()
# output = two_sum_finder.twoSum([3, 2, 4], 6)
# print(output)

two_sum_finder = Solution()
output = two_sum_finder.twoSum([3, 3], 6)
print(output)


# note to self: don't use the remove method, it removes the value from the initial array, even if you assign it to another variable beforehand
                
