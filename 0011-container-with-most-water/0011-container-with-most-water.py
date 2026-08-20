class Solution:
    def maxArea(self, height: List[int]) -> int:
        # res = 0

        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         area = (r-l) * min(height[l],height[r])
        #         res = max(area, res)
        # return res
       
       
        # res = 0
        # l, r = 0, len(height)-1

        # while l < r:
        #     area = (r-l) * min(height[l],height[r])
        #     res = max(area, res)

        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return res

        # res = 0

        # l = 0
        # r = len(height) - 1

        # while l < r:
        #     area = (r-l) * min(height[l], height[r])
        #     res = max(area, res)

        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return res



        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area



