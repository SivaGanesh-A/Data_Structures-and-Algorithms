class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans
        
        # n = len(temperatures)
        # ans = [0] * n

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = j - i
        #             break
        # return ans