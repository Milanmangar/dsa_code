# https://www.udemy.com/course/dynamic-programming-algorithms-coding-interview-questions/learn/lecture/38723278#overview


class Solution:
    # def path(self, paths):
    #     """
    #     recusive brute force
    #     Time: O(2^(n+m))
    #         n = each element length
    #         m = array length
    #     Space: O(m)
    #     """

    #     def answer(row, col):
    #         if (row >= len(paths) or col >= len(paths[0])) or (paths[row][col] == 1):
    #             return 0
    #         if row == len(paths) - 1 and col == len(paths[0]) - 1:
    #             return 1
    #         right_move = answer(row, col + 1)
    #         down_move = answer(row + 1, col)
    #         return right_move + down_move

    #     return answer(0, 0)

    # def path(self, paths):
    #     """
    #     optimized recusive
    #     Time: O(n*m)
    #         n = each element length
    #         m = array length
    #     Space: O(n * m) for memo table + O(n + m) for recursion stack
    #     """

    #     def answer(row, col, memo):
    #         if (row >= len(paths) or col >= len(paths[0])) or (paths[row][col] == 1):
    #             return 0
    #         if row == len(paths) - 1 and col == len(paths[0]) - 1:
    #             return 1
    #         if memo[row][col] != -1:
    #             return memo[row][col]
    #         right_move = answer(row, col + 1, memo)
    #         down_move = answer(row + 1, col, memo)
    #         memo[row][col] = right_move + down_move
    #         return memo[row][col]

    #     memo = [[-1] * len(paths[0]) for _ in range(len(paths))]
    #     return answer(0, 0, memo)

    # def path(self, paths):
    #     """
    #     optimized recusive 2D
    #     Time: O(n*m)
    #         n = each element length
    #         m = array length
    #     Space: O(n * m) for memo table + O(n + m) for recursion stack
    #     """

    #     memo = [[0] * (len(paths[0])) for _ in range(len(paths))]
    #     memo[0][0] = 1
    #     for row_index in range(len(paths)):
    #         for col_index in range(len(paths[0])):
    #             top = 0
    #             left = 0
    #             if paths[row_index][col_index] == 0:
    #                 if row_index == 0 and col_index == 0:
    #                     continue
    #                 top = memo[row_index - 1][col_index] if (row_index - 1) >= 0 else 0
    #                 left = memo[row_index][col_index - 1] if (col_index - 1) >= 0 else 0
    #             memo[row_index][col_index] = top + left

    #     return memo[len(paths) - 1][len(paths[0]) - 1]

    # def path(self, paths):
    #     """
    #     optimized recusive 2D
    #     Time: O(n*m)
    #         n = each element length
    #         m = array length
    #     Space: O(n * m) for memo table + O(n + m) for recursion stack
    #     """
    #     if paths[0][0] == 1 or paths[len(paths) - 1][len(paths[0]) - 1] == 1:
    #         return 0
    #     memo = [[0] * (len(paths[0])) for _ in range(len(paths))]
    #     memo[0][0] = 1
    #     for row_index in range(len(paths)):
    #         for col_index in range(len(paths[0])):
    #             top = 0
    #             left = 0
    #             if paths[row_index][col_index] == 0:
    #                 if row_index == 0 and col_index == 0:
    #                     continue
    #                 top = memo[row_index - 1][col_index] if (row_index - 1) >= 0 else 0
    #                 left = memo[row_index][col_index - 1] if (col_index - 1) >= 0 else 0
    #             memo[row_index][col_index] = top + left

    #     return memo[len(paths) - 1][len(paths[0]) - 1]

    def path(self, paths):
        """
        optimized recusive 1D
        Time: O(n*m)
            n = each element length
            m = array length
        Space: O(n * m)
        """

        if paths[0][0] == 1 or paths[len(paths) - 1][len(paths[0]) - 1] == 1:
            return 0

        rows, cols = len(paths), len(paths[0])
        dp = [0] * cols  # Represents the current row
        dp[0] = 1

        for row in range(rows):
            for col in range(cols):
                if paths[row][col] == 1:
                    dp[col] = 0  # Obstacle: no path to this cell
                elif col > 0:
                    dp[col] += dp[col - 1]  # Add paths from the left
                    # dp[col] (top) already exists, add left

        return dp[-1]  # Bottom-right corner


s = Solution()
print(s.path([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))  # 0
print(s.path([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))  # 6
print(s.path([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
print(s.path([[0, 1], [0, 0]]))  # 1
