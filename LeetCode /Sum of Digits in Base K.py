class Solution:
    def sumBase(self, n: int, k: int) -> int:
        su = 0
        while n>0:
            s = n%k
            n = n//k
            su += s
        return su
        
Example 1:

Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
Example 2:

Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1.
