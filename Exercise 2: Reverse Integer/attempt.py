class Solution:
    def reverse(self, x: int) -> int:
        num_string = str(abs(x))
        if x < 0:
            reversed_string = num_string[::-1] # reverse string using slicing
            reversed_int = int(reversed_string) * -1
        else:
            reversed_string = num_string[::-1] # reverse string using slicing
            reversed_int = int(reversed_string)
        if reversed_int < (-2**31) or reversed_int > (2**31 - 1):
            return 0
        else:
            return reversed_int
        
reverse_int = Solution()
print(reverse_int.reverse(123))
