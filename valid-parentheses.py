"""
=== The Leetcode Journey ===
Longest Substring Without Repeating Characters
Roger Lam
2021-04-23

=== Question Description ===
Given a string s, find the length of the longest substring without repeating characters.

=== Solution Description ===
Double pointer solution with n squared run time.
"""
import math
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSubString = {}
        currSubStringLen = 0
        maxLen = 0
        strlen = len(s)
        i1 = 0
        i2 = 0
        
        # Loop through every character
        while i2 < strlen:
            # Increase substring length and add to current substring if 
            # current character not duplicate
            if not s[i2] in currSubString.keys():
                currSubString[s[i2]] = 1
                currSubStringLen += 1
            else:
                # Record old substring, possibly update max substring len
                if maxLen < currSubStringLen:
                    maxLen = currSubStringLen
                currSubString = {}
                currSubString[s[i2]] = 1
                currSubStringLen = 1

                # Work backwards in substring to check existence of valid
                # substring
                i1 = i2 - 1
                duped = False
                while not duped:
                    if not s[i1] in currSubString.keys():
                        currSubString[s[i1]] = 1
                        currSubStringLen +=1
                        i1 -= 1
                    else:
                        duped = True

                i1 = i2

            i2 += 1
            
        # Case that no duplicate characters are found
        if maxLen < currSubStringLen:
            return currSubStringLen

        return maxLen

solution = Solution()
inputString = "dvdf"
print("dvdf")
print(solution.lengthOfLongestSubstring(inputString))