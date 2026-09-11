import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        

        heap = []
        for row in range(len(matrix)):
            value = matrix[row][0]
            heapq.heappush(heap, (value, row, 0))
        for i in range(k):
            value, row, col = heapq.heappop(heap)
            next_col = col + 1
            
            if next_col < len(matrix[row]):
                next_val = matrix[row][next_col]

                heapq.heappush(heap, (next_val, row, next_col))
        return value        
        
        # heap = []
        # n = len(matrix)
        # for row in range(n):
        #     heapq.heappush(heap, (matrix[row][0], row, 0))
        # for _ in range(k):
        #     value, row, col = heapq.heappop(heap)
        #     if col + 1 < n:
        #         heapq.heappush(heap, (matrix[row][col+1], row, col +1))
        # return value