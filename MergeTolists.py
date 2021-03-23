#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: MergeTolists.py.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from copy import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = copy(l1)
        l2 = copy(l2)
        if l1 is None:
            return l2

        elif l2 is None:
            return l1

        res = l1 if l1.val < l2.val else l2

        if l1.val < l2.val:
            res.next = self.mergeTwoLists(l1.next, l2)  # 3
            # return l1
        else:
            res.next = self.mergeTwoLists(l2.next, l1)  # 1 2 4 5
            # return l2

        return res

    def reverse_node(self, l1: ListNode):
        if l1 is None or l1.next is None:
            return l1

        # new_node = l1
        new_node = self.reverse_node(l1.next)

        t1 = l1.next
        t1.next = l1
        l1.next = None
        #
        return new_node

    def merge_bali(self, l1: ListNode, l2: ListNode):
        prehead = ListNode(-1001)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 if l1 is not None else l2
        return prehead.next


def qingwa(n, tmp_data):
    # tmp_data = {}
    if n <= 2:
        return n

    if tmp_data.get(n) is not None:
        return tmp_data.get(n)

    ret = qingwa(n - 1, tmp_data) + qingwa(n - 2, tmp_data)
    tmp_data[n] = ret
    return tmp_data[n]


if __name__ == '__main__':
    tmp_data = {}
    # l1_val = [1, 2, 4]
    # l2_val = [1, 3, 4]
    l1 = ListNode(1)
    l11 = ListNode(2)
    l111 = ListNode(4)
    l1.next = l11
    l11.next = l111

    l2 = ListNode(1)
    l22 = ListNode(3)
    l222 = ListNode(4)

    l2.next = l22
    l22.next = l222

    # ret = Solution().mergeTwoLists(l1, l2)
    # print(ret.val)
    # print(ret.next.val)
    # print(ret.next.next.val)
    # print(ret.next.next.next.val)
    # print(ret.next.next.next.next.val)
    # print(ret.next.next.next.next.next.val)
    # #
    # print('='*20)
    # print(l2.next.val)
    # ret = Solution().merge_bali(l1, l2)
    # print(ret.val)
    # print(ret.next.val)
    # print(ret.next.next.val)
    # print(ret.next.next.next.val)
    # print(ret.next.next.next.next.val)
    # print(ret.next.next.next.next.next.val)
    # print('='*20)
    # print(l2.next.val)

    # ret = Solution().reverse_node(l1)
    # print(ret.val)
    # print(ret.next.val)
    # print(ret.next.next.val)

    x = qingwa(10, tmp_data)
    print(x)
