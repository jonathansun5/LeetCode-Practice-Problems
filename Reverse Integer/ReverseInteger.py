"""
https://leetcode.com/problems/reverse-integer/description/

7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x == 0:
            return 0
        if x < 0:
            negative = True
            x = -x
        if (int(str(x)[::-1]) > (2**31 - 1)) or (int(str(x)[::-1]) < (-2**31)):
            return 0
        else:
            if negative is True:
                return int('-' + str(x)[::-1])
            return int(str(x)[::-1])
