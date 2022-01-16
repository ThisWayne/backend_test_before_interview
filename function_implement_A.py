"""
Python 3
Given a string s, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Constraints:
• 1 <= s.length <= 2 * 105
• s consists only of printable ASCII characters.
"""


class Solution:

    # Time complexity: O(n)
    # Space complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    testcases = [
        ("  ", True),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("abba", True),
        ("abcba", True),
    ]

    solution = Solution()
    for i, testcase in enumerate(testcases):
        output = solution.isPalindrome(testcase[0])
        result = "Accepted" if output == testcase[1] else "Failed"
        print(
            (f'{i}: {result}, testcase: {testcase[0]}, expected: {testcase[1]}, output: {output}'))
