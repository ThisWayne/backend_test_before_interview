"""
Python 3
You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid. For example, strs =
["abc", "bce", "cae"] can be arranged as:
abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), 
columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, 
so you would delete column 1.
Return the number of columns that you will delete.

Constraints:
• n == strs.length
• 1 <= n <= 100
• 1 <= strs[i].length <= 1000
• strs[i] consists of lowercase English letters.
"""


from typing import List


class Solution:

    # Time complexity: O(mn), m: strs[i].length, n: strs.length
    # Space complexity: O(1)
    def minDeleteSizeForColSorted(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            for row in range(len(strs) - 1):
                if ord(strs[row][col]) > ord(strs[row + 1][col]):
                    count += 1
                    break
        return count


if __name__ == '__main__':
    testcases = [
        (["abc", "bce", "cae"], 1),
        (["a", "b"], 0),
        (["zyx", "wvu", "tsr"], 3),
    ]

    solution = Solution()
    for i, testcase in enumerate(testcases):
        output = solution.minDeleteSizeForColSorted(testcase[0])
        result = "Accepted" if output == testcase[1] else "Failed"
        print(
            (f'{i}: {result}, testcase: {testcase[0]}, expected: {testcase[1]}, output: {output}'))
