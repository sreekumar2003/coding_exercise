class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len( nums[0])
        for i in range(2**l):
            s = f'{i:0{l}b}'
            if s not in nums:
                return s


Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
