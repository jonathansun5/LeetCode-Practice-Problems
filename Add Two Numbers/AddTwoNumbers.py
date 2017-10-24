"""
https://leetcode.com/problems/add-two-numbers/description/

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        x = ListNode(0)
        y = x
        while l1 or l2 or carry:
            if l1 != None:
                l1number = l1.val
                l1 = l1.next
            else:
                l1number = 0
            if l2 != None:
                l2number = l2.val
                l2 = l2.next
            else:
                l2number = 0
            sumOfDigits = (l1number + l2number + carry) % 10
            carry = (l1number + l2number + carry) // 10
            x.next = ListNode(sumOfDigits)
            x = x.next
        return y.next
