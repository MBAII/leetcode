# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        add1 = 0
        p1 = l1
        p2 = l2
        result = None
        last = None
        while((p1 != None) or (p2 != None)):
            v1 = 0
            v2 = 0
            if p1 != None:
                v1 = p1.val
                p1 = p1.next
            if p2 != None:
                v2 = p2.val
                p2 = p2.next
            v = v1 + v2
            if (add1 == 1):
                v += 1
            if (v > 9):
                v -= 10
                add1 = 1
            else:
                add1 = 0
            new = ListNode(v)
            if (result == None):
                result = new
                last = new
            else:
                last.next = new
                last = last.next
        if add1 == 1:
            new = ListNode(1)
            last.next = new
        return result
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """