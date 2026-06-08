class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for nums in range(2,num+1):
            sums = 0
            for i in str(nums):
                sums = int(i)+sums
            if sums %2 ==0:
                count+=1

        return count

        
