class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = {')': '(', '}': '{', ']': '['}
        found_parentheses = []
        for char in s:
            if char in valid_parentheses.values():
                # if an opening bracket is found, add it to the array of found brackets
                found_parentheses.append(char)
            elif char in valid_parentheses.keys():
                closing_bracket = char
                # if an opening bracket in string, check if corresponding closing bracket exists in string
                if found_parentheses == []:
                    # if closing bracket wasn't found, return false
                    return False
                elif valid_parentheses[closing_bracket] != found_parentheses.pop(-1):
                    # if corrrsponding closing bracket not equal to the latest character found, return false
                    return False
            else:
                # character is not a parenthese, return false
                return False
        # otherwise return true
        return found_parentheses == []
