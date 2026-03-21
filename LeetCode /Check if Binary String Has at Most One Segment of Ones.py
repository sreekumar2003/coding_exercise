class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s.strip("0")

  Example 1:

Input: s = "1001"
Output: false
Explanation: The string has two segments of size 1.
Example 2:

Input: s = "110"
Output: true
