class Solution:
    def setZeroes(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        col0 = False

        for r in range(m):
            if matrix[r][0] == 0:
                col0 = True

            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for c in range(n):
                matrix[0][c] = 0
        if col0:
            for r in range(m):
                matrix[r][0] = 0









        # rows = len(matrix)
        # cols = len(matrix[0])
        # zero_pos = []

        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             zero_pos.append((i,j))
        # for row, col in zero_pos:
        #     for j in range(cols):
        #         matrix[row][j] = 0
        #     for i in range(rows):
        #         matrix[i][col] = 0


        # rows = len(matrix)
        # cols = len(matrix[0])
        # zero_positions = []

        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             zero_positions.append((i,j))

        # for row, col in zero_positions:
        #     for j in range(cols):
        #         matrix[row][j] = 0
        #     for i in range(rows):
        #         matrix[i][col] = 0