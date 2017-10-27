"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        odd = True
        medianIndex = (length1 + length2) // 2
        if (length1 + length2) % 2 == 0:
            odd = False
        combined = []
        indexPosition = 0
        while indexPosition < medianIndex + 1:
            if not nums1:
                combined.append(nums2[0])
                nums2 = nums2[1:]
            elif not nums2:
                combined.append(nums1[0])
                nums1 = nums1[1:]
            elif nums1[0] < nums2[0]:
                combined.append(nums1[0])
                nums1 = nums1[1:]
            else:
                combined.append(nums2[0])
                nums2 = nums2[1:]
            indexPosition += 1
        if odd:
            median = combined[medianIndex]
        else:
            median = float((combined[medianIndex - 1] + combined[medianIndex])) / 2
        return median
