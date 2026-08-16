class Solution:
    def fib(self, n: int) -> int:
        #Iterative O(n)
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b


        #Recursion with Meomoization O(n)

        # memo = [-1] * (n+1)
        # def solve(n):
        #     if n == 0:
        #         return 0
        #     if n == 1:
        #         return 1
        #     if memo[n] != -1:
        #         return memo[n]
        #     memo[n] = solve(n-1) + solve(n-2)
        #     return memo[n]
        # return solve(n)


        #Completely Recusive O(2*n)

        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # else:
        #     return self.fib(n-1) + self.fib(n-2)