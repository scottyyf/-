#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: pingheng_ercha.py.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)

    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0

            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True

        return abs(
            height(root.left) - height(root.right)) <= 1 and self.isBalanced(
            root.right) and self.isBalanced(root.left)
