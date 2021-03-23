#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: dp_learn.py.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2021, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
# 动态规划：
# 当前阶段和上下阶段都有关系   （--> 相当于人生的阶段）
# 阶段用k表示
# 状态： S[k]
# 无后效性： 假设选择了当前的状态， 那么后续的状态只和这个状态有关，和这个当前状态之前的状态没有关系
# （如何理解： 人生的选择， 你当前选择的东西只会影响到后面的路，而不会影响之前的路）

# 决策： 当前状态，可选择的状态 X[k] , 决策变量取值的范围D[k]

# 策略： 从头到尾 选择的一种 路径 。。 相当于 每一个人的 选择走的方式
# 最优策略： 所有策略中最好的那个， 比如 人的最好是当主席？ P1,n

## 状态转移方程： 一个状态到另一个状态的表示方程
## 指标函数： 衡量指标
