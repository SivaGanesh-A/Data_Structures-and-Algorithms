class Solution:
    def checkDivisibility(self, n: int) -> bool:
        c = str(n)
        summ = 0
        prod = 1
        for i in c:
            summ += int(i)
            prod *= int(i)
        return n % (summ + prod) == 0