# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/


class Solution:

    # def countSquares(self, matrix: list[list[int]]) -> int:
    # """
    # recursion with brute force
    # Space: O(m * n * 3^k)
    #     m = number of rows
    #     n = number of columns
    #     k is the minimum of m and n
    # Time: O(m + n)
    #     m = number of rows
    #     n = number of columns
    # """

    #     def count_sq_matrices(matrix, row_index, column_index):
    #         if (
    #             row_index >= len(matrix)
    #             or column_index >= len(matrix[1])
    #             or matrix[row_index][column_index] == 0
    #         ):
    #             return 0
    #         right = count_sq_matrices(matrix, row_index, column_index + 1)
    #         bottom = count_sq_matrices(matrix, row_index + 1, column_index)
    #         bottom_right = count_sq_matrices(matrix, row_index + 1, column_index + 1)
    #         return 1 + min(right, min(bottom, bottom_right))

    #     count = 0
    #     for row_index in range(len(matrix)):
    #         for column_index in range(len(matrix[row_index])):
    #             if matrix[row_index][column_index] == 1:
    #                 count += count_sq_matrices(matrix, row_index, column_index)
    #     return count

    # def countSquares(self, matrix: list[list[int]]) -> int:
    #     """
    #     recursion with memoization
    #     Space: O(m * n)
    #         m = number of rows
    #         n = number of columns
    #     Time: O(m * n)
    #     """

    #     def count_sq_matrices(matrix, row_index, column_index, table):
    #         if (
    #             row_index >= len(matrix)
    #             or column_index >= len(matrix[1])
    #             or matrix[row_index][column_index] == 0
    #         ):
    #             return 0
    #         if table[row_index][column_index] != -1:
    #             return table[row_index][column_index]
    #         right = count_sq_matrices(matrix, row_index, column_index + 1, table)
    #         bottom = count_sq_matrices(matrix, row_index + 1, column_index, table)
    #         bottom_right = count_sq_matrices(
    #             matrix, row_index + 1, column_index + 1, table
    #         )
    #         table[row_index][column_index] = 1 + min(right, min(bottom, bottom_right))
    #         return table[row_index][column_index]

    #     count = 0
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     table = [[-1] * col for _ in range(row)]
    #     for row_index in range(row):
    #         for column_index in range(col):
    #             if matrix[row_index][column_index] == 1:
    #                 count += count_sq_matrices(matrix, row_index, column_index, table)
    #     return count

    # def countSquares(self, matrix: list[list[int]]) -> int:
    #     """
    #     recursion with memoization with extra if else condition
    #     Space: O(m * n)
    #         m = number of rows
    #         n = number of columns
    #     Time: O(m * n)
    #     """

    #     def count_sq_matrices(matrix, row_index, column_index, table):
    #         if (
    #             row_index >= len(matrix)
    #             or column_index >= len(matrix[1])
    #             or matrix[row_index][column_index] == 0
    #         ):
    #             return 0
    #         if table[row_index][column_index] != -1:
    #             return table[row_index][column_index]
    #         right = count_sq_matrices(matrix, row_index, column_index + 1, table)
    #         bottom = count_sq_matrices(matrix, row_index + 1, column_index, table)
    #         bottom_right = count_sq_matrices(
    #             matrix, row_index + 1, column_index + 1, table
    #         )
    #         table[row_index][column_index] = 1 + min(right, min(bottom, bottom_right))
    #         return table[row_index][column_index]

    #     count = 0
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     table = [[-1] * col for _ in range(row)]
    #     for row_index in range(row):
    #         for column_index in range(col):
    #             if (
    #                 matrix[row_index][column_index] == 1
    #                 and table[row_index][column_index] == -1
    #             ):
    #                 count += count_sq_matrices(matrix, row_index, column_index, table)
    #             elif table[row_index][column_index] != -1:
    #                 count += table[row_index][column_index]
    #     return count

    # def countSquares(self, matrix: list[list[int]]) -> int:
    #     """
    #     tabular 2D
    #     Space: O(m * n)
    #         m = number of rows
    #         n = number of columns
    #     Time: O(m * n)
    #     """
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     table = [[0] * col for _ in range(row)]
    #     count = 0
    #     for curr_row_index in range(row):
    #         for curr_col_index in range(col):
    #             if matrix[curr_row_index][curr_col_index] == 1:
    #                 table[curr_row_index][curr_col_index] = 1 + min(
    #                     table[curr_row_index - 1][curr_col_index],
    #                     table[curr_row_index][curr_col_index - 1],
    #                     table[curr_row_index - 1][curr_col_index - 1],
    #                 )
    #                 count += table[curr_row_index][curr_col_index]
    #     return count

    def countSquares(self, matrix: list[list[int]]) -> int:
        """
        tabular 1D
        Space: O(m * n)
            m = number of rows
            n = number of columns
        Time: O(n)
            table: of size n
        """
        row = len(matrix)
        col = len(matrix[0])
        table = [0] * col
        count = 0
        for curr_row_index in range(row):
            curr_table = [0] * col
            for curr_col_index in range(col):
                if matrix[curr_row_index][curr_col_index] == 1:
                    curr_table[curr_col_index] = 1 + min(
                        table[curr_col_index],
                        curr_table[curr_col_index - 1],
                        table[curr_col_index - 1],
                    )
                    count += curr_table[curr_col_index]
            table = curr_table
        return count


s = Solution()
print(s.countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))  # 15
print(s.countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))  # 7
