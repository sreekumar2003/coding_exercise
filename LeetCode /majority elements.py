class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        v = max(set(nums), key=nums.count)
        return v
