import doctest

"""
Link: https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
"""

"""
Brute-Force Approach:
1. Take min of length of word1, word2, say m
2. Set new_word = empty string
3. Iterate from 0-m say i
    3.1. For each word1 at position i, append to new_word
    3.2. Repeat 3.1. for word2
4. Append remaining letter from position m to end for both word1,and word2 to new_word

Time complexity: 
    - Step (1) - max(length of word1, length of word2) = O(max(n,m)) = O(m)
    - Step (3) - O(n)
    - Step (4) - O(m-n)
    Total = 2x O(m)

Space complexity:
    O(m+n)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pass


    def merge_brute_force(self, word1: str, word2: str) -> str:
        """
        Equal word length
        >>> Solution().merge_brute_force("abc", "pqr")
        'apbqcr'

        Word1 is small
        >>> Solution().merge_brute_force("ab", "pqrs")
        'apbqrs'

        Word1 is big
        >>> Solution().merge_brute_force("abcd", "pq")
        'apbqcd'
        """
        len_w1, len_w2 = len(word1), len(word2)
        min_len = min(len_w1, len_w2)
        new_word = ''
        for i in range(min_len):
            new_word += word1[i] + word2[i]
        
        new_word += word1[min_len: ] + word2[min_len: ]

        return new_word

    


if __name__ == "__main__":
    doctest.testmod(verbose=True)