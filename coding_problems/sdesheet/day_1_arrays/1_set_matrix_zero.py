"""Set Matrix Zero

Problem Statement:
Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0
and then return the matrix.

Link : https://takeuforward.org/data-structure/set-matrix-zero/
"""
import doctest
from typing import List

"""Example:
Input: 3 x 3 matrix
[
    [0, 0, 4],
    [7, 8, 6],
    [1, 2, 4],
]

Output:
[
    [0, 0, 0],
    [0, 0, 6],
    [0, 0, 4],
]
"""

"""Intuition:
Here, for any ij-th position if the value is 0, then values at every position 
- i-th row, any column, and
- any row, j-th column
are set to be 0 
"""

"""Pseudocode:
Brute Force Approach:
--------------------

1. Set rows, and columns to its count, from array arr.
2. Traverse element from 0-th row to ending rows, i.e., i-th row.
3. Traverse element from 0-th col to ending columns, i.e., j-th column.
4. If arr[i][j] == 0,
5. Set, all elem after position (i, j) to -1
6. Set, all elem before position (i, j) to -1
7. Traverse element from 0-th row to ending rows, i.e., i-th row.
8. Traverse element from 0-th col to ending columns, i.e., j-th column.
9. If arr[i][j] == -1, then, set it to 0.

Time Complexity: O(n x m) * ( O(n-1) + O(m-1) ) + O(n x m) 
= O(n^2) x 2 O(n) + O(n^2)          If rows and columns are of equal size.
= O(n^3)
1. Time for setting -1 for rows, except that row-position = O(n-1)
2. Time for setting -1 for columns, except that column-position = O(m-1)
3. For every column traverse inside row traverse for searching value with 0 = O(n x m)
4. For every column traverse inside row traverse for searching value with -1 = O(n x m)


Better Approach ( Store row and column for value with 0):
--------------------------------------------------------

1. Set rows_count, and cols_count to its count, from array arr.
2. Set row_with_zeros, and col_with_zeros as array of size rows_count and cols_count respectively, with every element set to zero.
3. Traverse element from 0-th row to ending rows, i.e., i-th row.
4. Traverse element from 0-th col to ending columns, i.e., j-th column.
5. If arr[i][j] == 0,
6. Set, position at i-th in row_with_zeros to -1
7. Set, position at j-th in col_with_zeros to -1
8. For every row in row_with_zeros, with value as -1, say i
9. Traverse element from 0-th col to ending columns, i.e., j-th column, and set arr[i][j] = 0
10. For every col in col_with_zeros, with value as -1, say i
11. Traverse element from 0-th row to ending rows, i.e., j-th column, and set arr[i][j] = 0

Time Complexity: O( 2(N x M) )
Space Complexity: O(N) + O(M)
"""


class Solution:

    def brute_force_approach_set_matrix_zero(self, in_matrix: List[List[int]]):
        """
        >>> matrix = [[0, 0, 4],[7, 8, 6],[1, 2, 4],]
        >>> Solution().brute_force_approach_set_matrix_zero(matrix)
        [[0, 0, 0], [0, 0, 6], [0, 0, 4]]
        """
        rows_count = len(in_matrix)
        cols_count = len(in_matrix[0])
        for row_index, arr_row in enumerate(in_matrix):
            for col_index, elem in enumerate(arr_row):
                if elem == 0:
                    self.__set_element_to_neg_one_in_row(in_matrix, row_index, cols_count)
                    self.__set_element_to_neg_one_in_col(in_matrix, col_index, rows_count)

        # set every -1 to 0
        self.__set_element_with_neg_one_to_zero(in_matrix, rows_count, cols_count)

        return in_matrix

    @staticmethod
    def __set_element_to_neg_one_in_row(arr, row_index, cols_count):
        for col_index in range(cols_count):
            if arr[row_index][col_index] != 0:
                arr[row_index][col_index] = -1

    @staticmethod
    def __set_element_to_neg_one_in_col(arr, col_index, row_count):
        for row_index in range(row_count):
            if arr[row_index][col_index] != 0:
                arr[row_index][col_index] = -1

    @staticmethod
    def __set_element_with_neg_one_to_zero(arr, row_count, cols_count):
        for row_index in range(row_count):
            for col_index in range(cols_count):
                if arr[row_index][col_index] == -1:
                    arr[row_index][col_index] = 0

    def better_approach_set_matrix_zero(self, in_matrix: List[List[int]]):
        """
        >>> matrix = [[0, 0, 4],[7, 8, 6],[1, 2, 4],]
        >>> Solution().better_approach_set_matrix_zero(matrix)
        [[0, 0, 0], [0, 0, 6], [0, 0, 4]]
        """
        rows_count = len(in_matrix)
        cols_count = len(in_matrix[0])
        rows_with_zeros = [0] * rows_count
        cols_with_zeros = [0] * cols_count

        for row_index in range(rows_count):
            for col_index in range(cols_count):
                if in_matrix[row_index][col_index] == 0:
                    rows_with_zeros[row_index] = -1
                    cols_with_zeros[col_index] = -1

        # Now, set all element at (i, j) to 0, if rows_with_zeros[i]==-1 or cols_with_zeros[j] == -1
        for row_index in range(rows_count):
            for col_index in range(cols_count):
                if rows_with_zeros[row_index] == -1 or cols_with_zeros[col_index] == -1:
                    in_matrix[row_index][col_index] = 0

        return in_matrix


if __name__ == "__main__":
    doctest.testmod()
