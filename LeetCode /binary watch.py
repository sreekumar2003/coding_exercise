/*
Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []
*/
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range(12):
            for j in range(60):
                if bin(i).count("1")+bin(j).count("1") == turnedOn:
                    res.append(f"{i}:{j:02d}")
    
        return res
        
