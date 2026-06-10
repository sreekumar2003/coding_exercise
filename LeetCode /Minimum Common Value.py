class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if (set(nums2).intersection(set(nums1))):
            return min(set(nums2).intersection(set(nums1)))
        return -1
Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
