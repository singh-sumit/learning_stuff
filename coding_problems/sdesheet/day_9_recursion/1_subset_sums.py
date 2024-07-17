"""Subset Sum : Sum of all Subsets
Problem Statement:
Given an array print all the sum of the subset generated from it, in the increasing order.
"""
from typing import List

"""Example 1:

Input: N = 3, arr[] = {5,2,1}

Output: 0,1,2,3,5,6,7,8

Explanation: 
We have to find all the subset’s sum and print them.in this case the generated subsets are 
[ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],
so the sums we get will be  0,1,2,3,5,6,7,8

Input: N=3,arr[]= {3,1,2}

Output: 0,1,2,3,3,4,5,6

Explanation:
We have to find all the subset’s sum and print them.in this case the generated subsets are 
[ [], [1], [2], [2,1], [3], [3,1], [3,2]. [3,2,1],
so the sums we get will be  0,1,2,3,3,4,5,6
"""

"""Intuition:
size        subset numbers
4       =   1
3       =   4         
2       =   4
1       =   4
0       =   1

For a size (N/0) subset , subset counts = 1, else for other its N.
"""

class Solution:

    def iter_approach_generate_subsets(self, arr: List, n: int):
        for subset_size in range(n, 0 -1):
            pass

    def gen_subset(self, arr, n, subset_size):
        for index in range(n):
            yield arr[:index-2]+arr[index:index+subset_size]