"""N meetings in one room

Problem Statement: 
There is one meeting room in a firm. You are given two arrays, start and end each of size N.For an index ‘i’, start[i] denotes the starting time of the ith meeting while end[i]  will denote the ending time of the ith meeting. 
Find the maximum number of meetings that can be accommodated if only one meeting can happen in the room at a  particular time. 
Print the order in which these meetings will be performed.

Link: https://takeuforward.org/data-structure/n-meetings-in-one-room/
"""

"""Example:
Input:  N = 6,  start[] = {1,3,0,5,8,5}, end[] =  {2,4,5,7,9,9}

Output: 1 2 4 5
"""

"""Intution:
There can be two types of meetings, either one finishing early while other finishing late. Which one should we choose?
If our meeting lasts longer the room stays occupied and we loose our time. While on the other hand, if we choose a meeting that finishes early we can accommodate more meetings.
Hence, we should choose a meetings that ends early and utilize the remaining time for more meetings.
"""

"""Pseudocode:
1. Sort, the meetings based on `end` time array, in ascending order.
2. Create a variable `answer`. Set it to 1, as initially, the first meeting will be always performed.
3. Create a variable `limit` that keeps track of ending time of previous meeting. Initially sets to ending time of first meeting.
4. Start iterating from second meeting. At every position we have two posibilities:
    a. If the start time of meeting is strictly greater than `limit` we can perform this meeting. Update the answer, and limit with the ending time of current meeting.
    b. If the start time of meeting is less than or equal to `limit` skip and move ahead. ( As, this time is already covered. )
"""

"""
Time complexity: 
    O(nlogn)                       Sorting
    O(n)                           Comparing & Iterating
  = O(nlogn)                    Approx

Space Complexity:
    O(n)                        Storing performable meetings index
"""

from typing import List
from collections import namedtuple
import doctest

meeting = namedtuple('Meeting', ['start', 'end', 'pos'])

class Solution:

    def max_meetings(self, start: list[int], end: List[int], meeting_count: int):
        """
        >>> n = 6
        >>> start = [1, 3, 0, 5, 8, 5]
        >>> end = [2, 4, 5, 7, 9, 9]
        >>> Solution().max_meetings(start, end, n)
        [1, 2, 4, 5]
        """
        meets = [meeting(start[i], end[i], i+1) for i in range(meeting_count)]
        meets = sorted(meets, key=lambda meet: (meet.end, meet.pos))
        performable_meetings =[]
        performable_meetings.append(meets[0].pos)
        prev_end_time = meets[0].end

        for i in range(1, meeting_count):
            if meets[i].start > prev_end_time:
                prev_end_time = meets[i].end
                performable_meetings.append(meets[i].pos)

        # Order of performable meetings opting for maximum meetings
        return performable_meetings


if __name__ == "__main__":
    doctest.testmod()