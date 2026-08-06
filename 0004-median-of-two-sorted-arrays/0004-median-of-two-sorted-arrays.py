class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)

        l = 0
        r = m

        half = (m+n+1) // 2

        while l <= r:
            partX = (l+r) // 2
            partY = half - partX

            if partX == 0:
                Lx = float('-inf')
            else:
                Lx = nums1[partX - 1]
            if partX == m:
                Rx = float('inf')
            else:
                Rx = nums1[partX]

            if partY == 0:
                Ly = float('-inf')
            else:
                Ly = nums2[partY - 1]
            if partY == n:
                Ry = float('inf')
            else:
                Ry = nums2[partY]
            
            if Lx <= Ry and Ly <= Rx:
                if (m+n) % 2 == 0:
                    return (max(Lx, Ly) + min(Rx, Ry)) / 2
                else:
                    return max(Lx, Ly)
            if Lx > Ry:
                r = partX - 1
            else:
                l = partX + 1

        
        # nums = sorted(nums1 + nums2)
        # n = len(nums)
        # if (n % 2) != 0:
        #     middle = n//2
        #     median = nums[middle]
        #     return median
        # else:
        #     middle1 = n//2 -1
        #     middle2 = n//2
        #     median = (nums[middle1] + nums[middle2]) / 2
        #     return median
