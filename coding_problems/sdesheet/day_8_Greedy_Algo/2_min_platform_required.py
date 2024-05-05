"""Minimum number of platforms required for a railway

Problem Statement: We are given two arrays that represent the arrival and departure times of trains that stop at the platform. 
We need to find the minimum number of platforms needed at the railway station so that no train has to wait.

Examples 1:

Input: N=6, 
arr[] = {9:00, 9:45, 9:55, 11:00, 15:00, 18:00} 
dep[] = {9:20, 12:00, 11:30, 11:50, 19:00, 20:00}

Output:3
"""

"""Approach:
Pseudocode:
1. Sort both arr, dep based on ascending order of arr
2. Set `platform_max_wait_times` = []
3. Set `platform_max_wait_times` with first arrivals, dep time.
4. Iterate from 2nd arrival to last.
    There will be two conditions:
    a. Arrival time of i-th rail is >= wait time of platforms.
        4.1. Set the i-th rail dep time, as the wait time of that platform.
    b. Arrival time of i-th rail is < wait time of platfroms.
        4.2. Append the i-th rail dep time to `platform_max_wait_times`
5. The length of `platform_max_wait_times` is minimum number of platform required.

Dry Run:
arr[] = {9:00, 9:45, 9:55, 11:00, 15:00, 18:00} 
dep[] = {9:20, 12:00, 11:30, 11:50, 19:00, 20:00}
------------------------------------------------
platform_max_wait_times = [9:20, ]

Rail 2: 
    Arr- 9:45   Dep- 12:00

Since, Arr > platform_max_wait_times[0]
    Set, platform_max_wait_times[0] = Dep   = [12:00, ]

Rail 3:
    Arr- 9:55,  Dep- 11:30

Since, Arr < platform_max_wait_times[0]
    Append, this Dep
    Thus, platform_max_wait_times = [12:00, 11:30, ]

Rail 4:
    Arr- 11:00,  Dep- 11:50

Since, Arr < any i-th platform_max_wait_times
    Append, this Dep
    Thus, platform_max_wait_times = [12:00, 11:30, 11:50 ]

Rail 5:
    Arr- 15:00,     Dep- 19:00

Since, Arr > platform_max_wait_times[0]
    Set, platform_max_wait_times[0] = Dep 
    Thus,  = [ 19:00, 11:30, 11:50 ]

Rail 6:
    Arr- 18:00,     Dep- 20:00

Since, Arr > platform_max_wait_times[1]
    Set, platform_max_wait_times[1] = Dep
    Thus, = [ 19:00, 20:00, 11:50 ]
"""

from collections import namedtuple
import doctest

schedule = namedtuple('Schedule', ['arrival', 'depature'])


class Solution:

    def min_platform(self, arrivals, depatures, rails):
        """
        >>> rails = 6
        >>> arrivals=[900, 945, 955, 1100, 1500, 1800]
        >>> depatures=[920, 1200, 1130, 1150, 1900, 2000]
        >>> Solution().min_platform(arrivals, depatures, rails)
        3
        """

        rail_schedules = [schedule(arrivals[i], depatures[i]) for i in range(rails)]
        rail_schedules=sorted(rail_schedules, key=lambda schedule: schedule.arrival)
        
        platform_min_wait_times = [rail_schedules[0].depature]

        for i in range(1, rails):
            for platform in range(len(platform_min_wait_times)):
                if rail_schedules[i].arrival > platform_min_wait_times[platform]:
                    platform_min_wait_times[platform] = rail_schedules[i].depature
                    break
            else:
                platform_min_wait_times.append(rail_schedules[i].depature)
        
        # print("Platform min waiting times", platform_min_wait_times)

        return len(platform_min_wait_times)



if __name__ == "__main__":
    doctest.testmod()