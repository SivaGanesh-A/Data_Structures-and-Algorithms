class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        used = [False] * len(nums)

        def backtrack():
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                curr.append(nums[i])
                used[i] = True

                backtrack()

                used[i] = False
                curr.pop()
        backtrack()
        return result