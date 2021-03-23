#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: remove_dumplicate.py.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""


def remove_dumplicate(nums: list) -> int:
    slow = 0
    for k, v in enumerate(nums[1:]):
        if v not in nums[:slow]:
            slow += 1
            nums[slow] = v

    return slow + 1


if __name__ == '__main__':
    nums = [1, 1, 2]
    ret = remove_dumplicate(nums)
    print(ret)
    print(nums)
