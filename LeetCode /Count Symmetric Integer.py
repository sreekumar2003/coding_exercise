class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for i in range(low,high+1):
            le = len(str(i))
            i = str(i)
            if le % 2 != 0:
                continue
            lf = i[0:le//2]
            rf = i[le//2:le]
            rf = [int(i) for i in rf]
            lf = [int(i) for i in lf]
            if sum(lf)==sum(rf):
                c+=1
        return c

Example 1:

Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.
Example 2:

Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.


