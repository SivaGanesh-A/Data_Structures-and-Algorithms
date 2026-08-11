class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        seen = set(nums)
        miss_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                miss_num += nums[i]
            else:
                break
        while miss_num in seen:
            miss_num += 1
        return miss_num