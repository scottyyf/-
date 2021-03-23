#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: merge.py.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 快慢指针

        nums1_c = nums1[:m]
        nums1[:] = []

        slow = 0
        fast = 0
        while slow < m and fast < n:
            if nums1_c[slow] > nums2[fast]:
                nums1.append(nums2[fast])
                fast += 1
            elif nums1_c[slow] <= nums2[fast]:
                nums1.append(nums1_c[slow])
                slow += 1

        if fast < n:
            nums1.extend(nums2[fast:])
        if slow < m:
            nums1.extend(nums1_c[slow:])


if __name__ == '__main__':
    a = [1, 7, 8, 0, 0, 0]
    b = [2, 5, 6]
    Solution().merge(a, 3, b, len(b))
    print(a)
