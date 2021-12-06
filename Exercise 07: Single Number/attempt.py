class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single_number_found = False
        while not single_number_found:
            for num in nums:
                if nums.count(num) == 1:
                    return num
