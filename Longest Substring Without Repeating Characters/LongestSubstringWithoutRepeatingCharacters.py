"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        soFar = []
        maximum = 0
        for character in s:
            if character in soFar:
                count = len(soFar)
                if count > maximum:
                    maximum = count
                soFar = soFar[soFar.index(character) + 1:]
                soFar.append(character)
            else:
                soFar.append(character)
                count = len(soFar)
                if count > maximum:
                    maximum = count
        return maximum
