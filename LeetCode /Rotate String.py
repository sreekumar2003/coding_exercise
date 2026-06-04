class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        goal = list(goal)
        for i in s:
            v = s.pop(0)
            s.append(v)
            if s==goal:
                return True
        
        return False
Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
