class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currmax,currmin = 1,1
        for n in nums:

            temp = currmax*n
            currmax = max(temp,currmin*n,n)
            currmin = min(temp,currmin*n,n)
            res = max(currmax,res)
        return res

        
'''
Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''
