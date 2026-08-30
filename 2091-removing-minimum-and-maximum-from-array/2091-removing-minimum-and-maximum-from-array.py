class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn = min(nums)
        maxx = max(nums)

        a = nums.index(minn)
        b = nums.index(maxx)

        left = min(a, b)
        right = max(a, b)

        front = right + 1
        back = len(nums) - left
        both = left + 1 + len(nums) - right

        return min(front, back, both)