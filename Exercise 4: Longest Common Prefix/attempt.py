class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        shortest_word = min(strs, key=len)   # find shortest word in list
        strs.remove(shortest_word)  # remove shortest word from list
        for index in range(len(shortest_word)):  # for each index in the shortest word, check each the remaining strings in strs
            for string in strs:
                if index == len(string) or string[index] != shortest_word[index]:   # return prefix if index goes out of bounds, or if the string character does not equal the character in the shortest word at the same index
                    return longest_common_prefix
            # otherwise, the character in all strings are equal for that index. add it to the longest_common_prefix
            longest_common_prefix += shortest_word[index]  
        # if all letters in the shortest word matched the letters in all the strings
        return longest_common_prefix
