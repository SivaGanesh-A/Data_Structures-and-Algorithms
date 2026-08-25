class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_Set = set(nums)
        multiple = k
        while multiple in num_Set:
            multiple += k
        return multiple