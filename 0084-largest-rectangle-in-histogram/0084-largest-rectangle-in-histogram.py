class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n= len(heights)
        left = [-1] * n
        right = [n] * n
        
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        max_Area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_Area = max(max_Area, area)
        return max_Area

        # n = len(heights)
        # max_area = 0

        # for i in range(n):
            
        #     height = heights[i]
        #     left = i
        #     while left >= 0 and heights[left] >= height:
        #         left -= 1
            
        #     right = i
        #     while right < n and heights[right] >= height:
        #         right += 1

        #     width = right - left -1
        #     area = height * width

        #     max_area = max(max_area, area)
        # return max_area