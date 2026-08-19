class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        # ans = []
        # nums.sort()
        # n = len(nums)
        # for i in range(n):
        #     if i != 0 and nums[i] == nums[i-1]:
        #         continue
        #     j = i+1
        #     k = n-1
        #     while j < k:
        #         total_sum = nums[i] + nums[j] + nums[k]
        #         if total_sum > 0:
        #             k -= 1
        #         elif total_sum < 0:
        #             j += 1
        #         else:
        #             temp = [nums[i], nums[j], nums[k]]
        #             ans.append(temp)

        #             j += 1
        #             k -= 1

        #             while j < k and nums[j] == nums[j-1]:
        #                 j += 1
        #             while j < k and nums[k] == nums[k+1]:
        #                 k -= 1
        # return ans




        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ans







