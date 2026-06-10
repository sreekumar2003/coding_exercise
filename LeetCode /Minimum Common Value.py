class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if (set(nums2).intersection(set(nums1))):
            return min(set(nums2).intersection(set(nums1)))
        return -1
