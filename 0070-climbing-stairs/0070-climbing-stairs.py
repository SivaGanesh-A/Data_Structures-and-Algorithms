class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a+b
        return b
        # memo = [-1] * (n+1)
        # def solve(n):

        #     if n == 0 or n == 1:
        #         return 1
        #     if memo[n] != -1:
        #         return memo[n]
            
        #     memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        #     return memo[n]
        # return solve(n)