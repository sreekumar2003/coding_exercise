class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = f'{n:0b}'
        n = str(n)
        s = ""
        for i in n:
            if i=="0":
                s = s+"1"
            else:
                s = s+"0"
        
        return int(s,2)


Example 1:

Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 
