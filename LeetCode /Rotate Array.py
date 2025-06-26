class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       for i in range(k):
        m = nums.pop()
        nums.insert(0,m)
