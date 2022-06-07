class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_x = 0
        
        while x != 0:
            digit = x % 10  # Take the last remaining digit of x
            reversed_x = reversed_x * 10 + digit  # Pushes the previous digits back by multiplying them by ten while adding the next digit
            x = x // 10  # Turn the floor of x divided by 10
            
        return reversed_x
