"""
Search, Insert, and Delete in an Unsorted Array
Link: https://www.geeksforgeeks.org/search-insert-and-delete-in-an-unsorted-array/?ref=lbp
"""
import doctest
from array import array
from typing import Optional

"""
Operation:
- Search element:
    - Searching in un-sorted array, requires linear traversal O(n)
- Insertion:
    - Insertion is faster than sorted array, because we do not need to care about the required position to make the final array sorted again.
    - Inserting an element requires to shift element, (in worst case O(n))
    - time : O(n) space: O(1)
- Deletion: O(n)
    - Similar to insertion, we need to shift element after deletion.
    - Also, it is faster compared to in sorted array.
"""


class Array:

    def __init__(self, elements: Optional[list] = None):
        self.__arr = array('i', elements if elements else [])
        self.__size = len(elements) if elements else 0

    def find(self, elem: int) -> int:
        """
        >>> arr = Array([1,2,3,8,4,5])
        >>> arr.find(1)
        0
        >>> arr = Array([1,2,3,8,4,5])
        >>> arr.find(8)
        3
        >>> arr = Array([1,2,3,8,4,5])
        >>> arr.find(5)
        5
        >>> arr = Array([1,2,3,8,4,5])
        >>> arr.find(9)
        -1
        """
        position = -1
        for index in range(0, self.__size):
            if elem == self.__arr[index]:
                position = index
                break

        return position

    def insert(self, pos: int, elem: int):
        """
        >>> arr = Array([1,2,3,4,5])
        >>> arr
        [1, 2, 3, 4, 5]
        >>> arr.insert(2,9)
        >>> arr
        [1, 2, 9, 3, 4, 5]
        """
        self.__arr.append(0)
        for index in range(self.__size - 1, 0, -1):
            # shift towards end
            self.__arr[index + 1] = self.__arr[index]

            if pos == index:
                self.__arr[index] = elem
                self.__size += 1
                break

    def delete_at(self, pos: int):
        """
        >>> arr = Array()
        >>> arr.delete_at(0)
        Traceback (most recent call last):
            ...
        IndexError: Position 0 not in array of size :0
        >>> arr = Array([3,4,6,7])
        >>> arr.delete_at(1)
        >>> arr
        [3, 6, 7]
        >>> arr.delete_at(2)
        >>> arr
        [3, 6]
        >>> arr.delete_at(0)
        >>> arr
        [6]
        >>> arr.delete_at(0)
        >>> arr
        []
        >>> arr.delete_at(-1)
        Traceback (most recent call last):
            ...
        IndexError: Position -1 not in array of size :0
        """
        if not self.__is_position_in_range(pos):
            raise IndexError(f'Position {pos} not in array of size :{self.__size}')

        for index in range(pos, self.__size - 1):
            if self.__size == 1:
                self.__arr = []
            else:
                # shift element one position ahead
                self.__arr[index] = self.__arr[index + 1]

        self.__arr.pop(self.__size - 1)
        self.__size -= 1

    def __is_position_in_range(self, pos: int) -> bool:
        return 0 <= pos <= self.__size - 1

    def delete_elem(self, elem: int):
        """
        >>> arr = Array()
        >>> arr.delete_elem(1)
        >>> arr
        []

        >>> arr = Array([1,2,3,4])
        >>> arr.delete_elem(2)
        >>> arr
        [1, 3, 4]

        >>> arr.delete_elem(4)
        >>> arr
        [1, 3]

        >>> arr.delete_elem(8)
        >>> arr
        [1, 3]

        >>> arr.delete_elem(1)
        >>> arr
        [3]

        >>> arr.delete_elem(3)
        >>> arr
        []

        >>> arr.delete_elem(8)
        >>> arr
        []
        """
        is_present = False
        for index in range(self.__size):
            is_present = is_present or elem == self.__arr[index]
            is_last_position = index == self.__size-1
            if is_present and not is_last_position:
                # move element behind it ahead
                self.__arr[index] = self.__arr[index + 1]

        if is_present:
            self.__arr.pop(self.__size - 1)
            self.__size -= 1

    def __repr__(self):
        return f"{self.__arr.tolist()}"


if __name__ == "__main__":
    doctest.testmod()
