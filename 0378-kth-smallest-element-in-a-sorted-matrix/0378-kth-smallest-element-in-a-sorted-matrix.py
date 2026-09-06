import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        for row in range(n):
            heapq.heappush(heap, (matrix[row][0], row, 0))
        for _ in range(k):
            value, row, col = heapq.heappop(heap)
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col+1], row, col +1))
        return value