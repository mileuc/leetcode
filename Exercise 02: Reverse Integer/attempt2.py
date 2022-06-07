class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        absolute_value = str(abs(x))    # Take absolute value of x and convert to a string for indexing
        reversed_x = absolute_value[::-1]  # ::-1 corresponds to start:stop:step. When you pass -1 as step, the start point goes to the end and stop at the front.
        if -2**31 < x < 2**31:
            if x < 0:
                return int(reversed_x) * -1
            else:
                return int(reversed_x)
        else:
            return 0
