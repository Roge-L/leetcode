"""
=== The Leetcode Journey ===
Valid Parentheses
Roger Lam
2021-04-26

=== Question Description ===
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

=== Solution Description ===
Stack ADT implemented with a list; last in first out models valid parentheses well.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        
        for i in range(n):
            if s[i] == ")":
                if not stack:
                    return False
                prevpar = stack.pop()
                if prevpar != "(":
                    return False
            elif s[i] == "]":
                if not stack:
                    return False
                prevpar = stack.pop()
                if prevpar != "[":
                    return False
            elif s[i] == "}":
                if not stack:
                    return False
                prevpar = stack.pop()
                if prevpar != "{":
                    return False
            else:
                stack.append(s[i])
            
        if not stack:
            return True
            
        return False

solution = Solution()
inputString = "()[]{}"
print("()[]{}")
print(solution.isValid(inputString))