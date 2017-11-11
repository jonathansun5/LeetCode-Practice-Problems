"""
https://leetcode.com/problems/longest-palindromic-substring/description/

5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        maxLength = 1
        maxString = ""
        current1 = 0
        current2 = 0
        for index in xrange(1, len(s)):
            current1 = index - 1
            current2 = index
            while current1 >= 0 and current2 < len(s) and s[current1] == s[current2]:
                distance = current2 - current1 + 1
                if distance > maxLength:
                    maxLength = distance
                    maxString = s[current1 : current2 + 1]
                current1 -= 1
                current2 += 1
            current1 = index - 1
            current2 = index + 1
            while current1 >= 0 and current2 < len(s) and s[current1] == s[current2]:
                distance = current2 - current1 + 1
                if distance > maxLength:
                    maxLength = distance
                    maxString = s[current1 : current2 + 1]
                current1 -= 1
                current2 += 1
        if maxLength == 1:
            return s[0]
        return maxString
