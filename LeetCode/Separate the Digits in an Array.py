class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
       
        return [int(digit) for num in nums for digit in str(num)]
       
       
        # res = []
        # for i in nums:
        #     for j in str(i):
        #         res.append(int(j))
        
        # return res
        
            
        
        
        # nums = [str(i) for i in nums]
        # new = []
        # for i in nums:
        #     new.extend(list(i))
        # new = [int(i) for i in new]
        # return new

Example 1:

Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation: 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
Example 2:

Input: nums = [7,1,3,9]
Output: [7,1,3,9]
Explanation: The separation of each integer in nums is itself.
answer = [7,1,3,9].
 
        
