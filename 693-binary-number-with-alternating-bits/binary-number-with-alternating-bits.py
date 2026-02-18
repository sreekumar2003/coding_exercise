class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        deci = bin(n)[2:]
        for i in range(len(deci)-1):
            if deci[i]==deci[i+1]:
                return False
        return True
        