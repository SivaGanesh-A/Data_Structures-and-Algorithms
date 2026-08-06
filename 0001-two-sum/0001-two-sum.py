class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # seen = {}
        # for i, num in enumerate(nums):
        #     res = target - num
        #     if res in seen:
        #         return [seen[res],i]
        #     seen[num] = i

        seen = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in seen:
                return [seen[res], i]
            seen[num] = i

