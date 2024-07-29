"""
Search, Insert, and Delete in a Sorted Array
Link: https://www.geeksforgeeks.org/search-insert-and-delete-in-a-sorted-array/?ref=lbp
"""
import doctest
from array import array
from typing import Optional

"""
Operation:

- Searching element:
    - Binary Search can be used - O(log n)
- Insertion element:
    - Position is determined by binary search   O(log n)
    - And all element behind it are shifted     O(n)
    i.e. O(n)
- Deleting at a position:
    - Requires shifting an element to left part of an array, starting from a given position
    - O(n)

"""


class SortedArray:

    def __init__(self, elements: Optional[list] = None):
        self.__arr = array('i', elements if elements else [])
        self.__size = len(elements) if elements else 0

    def find(self, elem: int) -> int:
        """
        >>> arr = SortedArray([1,2,3,4,5])
        >>> arr.find(10)
        -1
        >>> arr.find(1)
        0
        >>> arr.find(4)
        3
        >>> arr.find(3)
        2
        >>> arr.find(5)
        4
        """
        position = self.__get_using_binary_search(elem)

        return position

    def __get_using_binary_search(self, elem: int):
        left = 0
        right = self.__size - 1
        while left <= right:
            mid = (left + right) // 2
            if elem == self.__arr[mid]:
                return mid
            elif elem > self.__arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def insert(self, elem: int):
        """
        >>> arr = SortedArray()
        >>> arr.insert(4)
        >>> arr
        [4]

        >>> arr = SortedArray([1,3,4,])
        >>> arr.insert(2)
        >>> arr
        [1, 2, 3, 4]
        >>> arr.insert(5)
        >>> arr
        [1, 2, 3, 4, 5]
        """
        position = self.__get_elem_pos_ahead(elem)
        self.__arr.append(0)

        # shift element
        for index in range(self.__size - 1, position - 1, -1):
            self.__arr[index + 1] = self.__arr[index]

        self.__arr[position] = elem
        self.__size += 1

    def __get_elem_pos_ahead(self, elem: int):
        last_identified_pos = -1
        left = 0
        right = self.__size - 1
        while left <= right:
            mid = (left + right) // 2
            if elem == self.__arr[mid]:
                last_identified_pos = mid
                return last_identified_pos
            elif elem > self.__arr[mid]:
                left = mid + 1
                last_identified_pos = left
            else:
                right = mid - 1
                last_identified_pos = right

        return last_identified_pos

    def delete_at(self, pos: int):
        """
        >>> arr = SortedArray()
        >>> arr.delete_at(1)
        >>> arr
        []

        >>> arr = SortedArray([1,2,3,4,5])
        >>> arr.delete_at(1)
        >>> arr
        [1, 3, 4, 5]
        >>> arr.delete_at(0)
        >>> arr
        [3, 4, 5]
        >>> arr.delete_at(2)
        >>> arr
        [3, 4]
        >>> arr.delete_at(2)
        >>> arr
        [3, 4]
        >>> arr.delete_at(1)
        >>> arr
        [3]
        >>> arr.delete_at(-1)
        >>> arr
        [3]
        >>> arr.delete_at(0)
        >>> arr
        []
        >>> arr.delete_at(0)
        >>> arr
        []
        """
        in_range = 0 <= pos <= self.__size - 1
        if not in_range:
            return

        # shift element to left of a position
        for index in range(pos, self.__size - 1):
            self.__arr[index] = self.__arr[index + 1]

        self.__arr.pop(self.__size - 1)
        self.__size -= 1

    def delete_elem(self, elem: int):
        pass

    def __repr__(self):
        return f"{self.__arr.tolist()}"


if __name__ == "__main__":
    doctest.testmod()
