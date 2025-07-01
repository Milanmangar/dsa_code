# https://www.udemy.com/course/dynamic-programming-algorithms-coding-interview-questions/learn/lecture/38718208#overview


class Solution:
    # def rod_cut(self, rod_lengths_opt, rod_prices, target_rod_len):
    #     """
    #     recusive brute force
    #     Time: O(2^n)
    #         n = target rod length
    #     Space: O(n)
    #     """

    #     def answer(rod_lengths_opt, rod_prices, target_rod_len, index):
    #         if target_rod_len <= 0 or index < 0:
    #             return 0

    #         cut = 0
    #         if rod_lengths_opt[index] <= target_rod_len:
    #             cut = rod_prices[index] + answer(
    #                 rod_lengths_opt,
    #                 rod_prices,
    #                 target_rod_len - rod_lengths_opt[index],
    #                 index,
    #             )
    #         not_cut = answer(rod_lengths_opt, rod_prices, target_rod_len, index - 1)
    #         return max(cut, not_cut)

    #     return answer(rod_lengths_opt, rod_prices, target_rod_len, len(rod_prices) - 1)

    # def rod_cut(self, rod_lengths_opt, rod_prices, target_rod_len):
    #     """
    #     optimized recusive with memoization
    #     Time: O(n * m)
    #         n = target rod length
    #         m = number of rod sizes

    #     Space: O(n * m)
    #         - memoization table: O(n * m)
    #         - recursion stack: O(n + m)
    #     """

    #     def answer(rod_lengths_opt, rod_prices, target_rod_len, index, table):
    #         # print(index, target_rod_len)
    #         if target_rod_len <= 0 or index < 0:
    #             return 0
    #         if table[index][target_rod_len] != -1:
    #             return table[index][target_rod_len]

    #         cut = 0
    #         if rod_lengths_opt[index] <= target_rod_len:
    #             cut = rod_prices[index] + answer(
    #                 rod_lengths_opt,
    #                 rod_prices,
    #                 target_rod_len - rod_lengths_opt[index],
    #                 index,
    #                 table,
    #             )
    #         not_cut = answer(
    #             rod_lengths_opt, rod_prices, target_rod_len, index - 1, table
    #         )
    #         table[index][target_rod_len] = max(cut, not_cut)
    #         return table[index][target_rod_len]

    #     table = [[-1] * (target_rod_len + 1) for _ in range(len(rod_lengths_opt))]
    #     return answer(
    #         rod_lengths_opt, rod_prices, target_rod_len, len(rod_prices) - 1, table
    #     )

    # def rod_cut(self, rod_lengths_opt, rod_prices, target_rod_len):
    #     """
    #     optimized with tabulation 2D
    #     Time: O(n * m)
    #         n = target rod length
    #         m = number of rod sizes

    #     Space: O(n * m)
    #     """

    #     table = [[0] * (target_rod_len + 1) for _ in range(len(rod_lengths_opt))]
    #     for index in range(len(rod_lengths_opt)):
    #         for curr_target_rod_len in range(target_rod_len + 1):
    #             cut = 0
    #             if rod_lengths_opt[index] <= curr_target_rod_len:
    #                 cut = (
    #                     rod_prices[index]
    #                     + table[index][curr_target_rod_len - rod_lengths_opt[index]]
    #                 )
    #             not_cut = table[index - 1][curr_target_rod_len]
    #             table[index][curr_target_rod_len] = max(cut, not_cut)
    #     return table[len(rod_lengths_opt) - 1][target_rod_len]

    # def rod_cut(self, rod_lengths_opt, rod_prices, target_rod_len):
    #     #     """
    #     #     optimized with tabulation 1D with temp table
    #     #     Time: O(n * m)
    #     #         n = target rod length
    #     #         m = number of rod sizes

    #     #     Space: O(n)
    #     #     """

    #     table = [0] * (target_rod_len + 1)
    #     for index in range(len(rod_lengths_opt)):
    #         temp_table = [0] * (target_rod_len + 1)
    #         for curr_target_rod_len in range(target_rod_len + 1):
    #             cut = 0
    #             if rod_lengths_opt[index] <= curr_target_rod_len:
    #                 cut = (
    #                     rod_prices[index]
    #                     + temp_table[curr_target_rod_len - rod_lengths_opt[index]]
    #                 )
    #             not_cut = table[curr_target_rod_len]
    #             temp_table[curr_target_rod_len] = max(cut, not_cut)
    #         table = temp_table
    #     return table[target_rod_len]

    def rod_cut(self, rod_lengths_opt, rod_prices, target_rod_len):
        #     """
        #     optimized with tabulation 1D without  temp table
        #     Time: O(n * m)
        #         n = target rod length
        #         m = number of rod sizes

        #     Space: O(n)
        #     """

        table = [0] * (target_rod_len + 1)
        for index in range(len(rod_lengths_opt)):
            for curr_target_rod_len in range(
                rod_lengths_opt[index], target_rod_len + 1
            ):
                cut = 0
                if rod_lengths_opt[index] <= curr_target_rod_len:
                    cut = (
                        rod_prices[index]
                        + table[curr_target_rod_len - rod_lengths_opt[index]]
                    )
                not_cut = table[curr_target_rod_len]
                table[curr_target_rod_len] = max(cut, not_cut)
        return table[target_rod_len]


s = Solution()
print(s.rod_cut([2], [5], 6))  # 9
print(s.rod_cut([1, 3, 4], [2, 7, 8], 4))  # 9
print(s.rod_cut([1, 2, 3, 4], [2, 3, 7, 8], 4))  # 9
print(s.rod_cut([1, 2, 3, 4, 5, 6], [2, 5, 8, 9, 10, 11], 6))  # 16
print(s.rod_cut([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))  # 14
