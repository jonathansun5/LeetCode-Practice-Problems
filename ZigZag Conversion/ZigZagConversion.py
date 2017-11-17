"""
https://leetcode.com/problems/zigzag-conversion/description/

6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == "" or numRows == 1 or numRows >= len(s):
            return s
        line = 0
        result = []
        while line < numRows:
            array1 = s[line :: 2 * (numRows - 1)]
            # either top row or bottom row
            if line == 0 or line == numRows - 1:
                result += array1
            else:
                array2 = s[line + 2 * (numRows - line - 1) :: 2 * (numRows - 1)]
                for i,v in enumerate(array2):
                    array1 = [str(r) for r in array1]
                    array1.insert(2 * i + 1,v)
                result += array1
            line += 1
        return ''.join(result)
