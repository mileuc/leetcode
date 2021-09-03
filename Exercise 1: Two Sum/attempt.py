class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    # has to return a list of integers
        solution_array = []
        # iterate through each number in the list and add that number to each of the other numbers in the list
        for first_number in nums:
            for second_number in nums:
                first_number_index = nums.index(first_number)
                second_number_index = nums.index(second_number)
                # if indices don't match, add the numbers
                if first_number_index != second_number_index:
                    sum_num = first_number + second_number
                    if sum_num == target:
                        # if number equals target, add index of each number to solution array
                        solution_array.append(first_number_index)
                        solution_array.append(second_number_index)
                        return solution_array
        print("No solution found.")                  
        return []
                          
two_sum_finder = Solution()
output = two_sum_finder.twoSum([2, 7, 11, 15], 9)
print(output)


# output = two_sum_finder.twoSum([3, 2, 4], 6)
# print(output)


# note to self: don't use the remove method, it removes the value from the initial array, even if you assign it to another variable beforehand
                
