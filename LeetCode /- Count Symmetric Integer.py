class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for i in range(low,high+1):
            le = len(str(i))
            i = str(i)
            if le % 2 != 0:
                continue
            lf = i[0:le//2]
            rf = i[le//2:le]
            rf = [int(i) for i in rf]
            lf = [int(i) for i in lf]
            if sum(lf)==sum(rf):
                c+=1
        return c


