from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = len(str1)
        s2 = len(str2)
        if str1+str2==str2+str1:
            value = gcd(s1,s2)
            return str1[0:value]
        else:
            return ""


Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
