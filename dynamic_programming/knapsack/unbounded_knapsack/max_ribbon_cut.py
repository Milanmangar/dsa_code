# https://www.udemy.com/course/dynamic-programming-algorithms-coding-interview-questions/learn/lecture/38718162#overview


class Solution:
    # def count_ribbon_pieces(self, sizes: list, n: int):
    #     """
    #     recusive brute force
    #     Time: O(2^m * n)
    #         n = target ribbon length
    #         m = number of sizes (len(sizes))
    #     Space: O(n + m)
    #     """

    #     def answer(sizes, ribbon_len, index):
    #         if ribbon_len == 0:
    #             return 0
    #         if index < 0:
    #             return -1
    #         take = -1
    #         if sizes[index] <= ribbon_len:
    #             take = answer(sizes, ribbon_len - sizes[index], index)
    #             if take != -1:
    #                 take = 1 + take
    #         not_take = answer(sizes, ribbon_len, index - 1)
    #         return max(take, not_take)

    #     return answer(sizes, n, len(sizes) - 1)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def count_ribbon_pieces(self, sizes: list, n: int):
        """
        optimized recursive with memoization
        Time: O(m * n)
            n = target ribbon length
            m = number of sizes (len(sizes))
        Space: O(n * m)
        """

        def answer(sizes, ribbon_len, index, table):
            if ribbon_len == 0:
                return 0
            if index < 0:
                return -1
            if table[index][ribbon_len] != -1:
                return table[index][ribbon_len]
            take = -1
            if sizes[index] <= ribbon_len:
                take = answer(sizes, ribbon_len - sizes[index], index, table)
                if take != -1:
                    take = 1 + take
            not_take = answer(sizes, ribbon_len, index - 1, table)
            table[index][ribbon_len] = max(take, not_take)
            return table[index][ribbon_len]

        table = [[-1] * (n + 1) for _ in range(len(sizes) + 1)]
        return answer(sizes, n, len(sizes) - 1, table)

    def count_ribbon_pieces(self, sizes: list, n: int):
        """
        Tabular 1D
        Time: O(m * n)
            n = target ribbon length
            m = number of sizes (len(sizes))
        Space: O(n)
        """

        table = [-1] * (n + 1)
        table[0] = 0
        for i in range(len(sizes)):
            for curr_capacity in range(1, n + 1):
                take = -1
                if sizes[i] <= curr_capacity and table[curr_capacity - sizes[i]] != -1:
                    take = 1 + table[curr_capacity - sizes[i]]
                not_take = table[curr_capacity]
                table[curr_capacity] = max(take, not_take)

        return table[n]


s = Solution()
print(s.count_ribbon_pieces([1, 2, 3], 5))  # 5
print(s.count_ribbon_pieces([2, 3, 5], 13))  # 6
print(s.count_ribbon_pieces([3, 5, 8], 13))  # 3
print(s.count_ribbon_pieces([1, 2, 5], 0))  # 0
