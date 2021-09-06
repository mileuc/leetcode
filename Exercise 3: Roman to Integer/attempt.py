class Solution:
    def romanToInt(self, s: str) -> int:
        int_value = 0
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # roman numerals are typically written from largest to smallest
        for index in range(len(s)):
            # check if index + 1 is still in bounds and the current character is smaller than the next
            # if a smaller numeral is written before a larger one, the value is subtracted
            if index + 1 < len(s) and roman_dict[s[index]] < roman_dict[s[index + 1]]:
                int_value -= roman_dict[s[index]]
            else:
                int_value += roman_dict[s[index]]
        return int_value
