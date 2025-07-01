class Solution:
    # def knapSack(self, val, wt, capacity):
    #     """
    #     recusive brute force
    #     Time: O(2^n)
    #         n: number of items
    #     Space: O(n)
    #     """

    #     def unbounded_knapsack(val, wt, capacity, index):
    #         if capacity <= 0:
    #             return 0
    #         if index == 0:
    #             return int(capacity / wt[index]) * val[index]
    #         take = 0
    #         if wt[index] <= capacity:
    #             take = val[index] + unbounded_knapsack(
    #                 val, wt, capacity - wt[index], index
    #             )
    #         not_take = unbounded_knapsack(val, wt, capacity, index - 1)
    #         return max(take, not_take)

    # def knapSack(self, val, wt, capacity):
    #     """
    #     optimized recusive with memoization
    #     Time: O(n * c)
    #         n: number of items
    #         c: capacity
    #     Space: O(n * c)
    #     """

    #     def unbounded_knapsack(val, wt, capacity, index, table):
    #         if capacity <= 0:
    #             return 0
    #         if index == 0:
    #             return int(capacity / wt[index]) * val[index]
    #         if table[index][capacity] != -1:
    #             return table[index][capacity]
    #         take = 0
    #         if wt[index] <= capacity:
    #             take = val[index] + unbounded_knapsack(
    #                 val, wt, capacity - wt[index], index, table
    #             )
    #         not_take = unbounded_knapsack(val, wt, capacity, index - 1, table)
    #         table[index][capacity] = max(take, not_take)
    #         return table[index][capacity]

    #     wt_len = len(val)
    #     table = [[-1] * (capacity + 1) for _ in range(wt_len)]
    #     return unbounded_knapsack(val, wt, capacity, wt_len - 1, table)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # def knapSack(self, val, wt, capacity):
    #     """
    #     optimized tabular 2D
    #     Time: O(n * c)
    #         n: number of items
    #         c: capacity
    #     Space: O(n * c)
    #     """

    #     def unbounded_knapsack(val, wt, capacity):
    #         table = [[0] * (capacity + 1) for _ in range(len(wt))]
    #         for i in range(len(wt)):
    #             for curr_capacity in range(capacity + 1):
    #                 if i == 0:
    #                     table[i][curr_capacity] = int(curr_capacity / wt[i]) * val[i]
    #                 else:
    #                     include = 0
    #                     if wt[i] <= curr_capacity:
    #                         include = val[i] + table[i][curr_capacity - wt[i]]

    #                     table[i][curr_capacity] = max(
    #                         include, table[i - 1][curr_capacity]
    #                     )
    #         return table[len(val) - 1][capacity]

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def knapSack(self, val, wt, capacity):
        """
        optimized tabular 1D
        Time: O(n * c)
            n: number of items
            c: capacity
        Space: O(c)
        """

        def unbounded_knapsack(val, wt, capacity):
            table = [0] * (capacity + 1)
            for i in range(len(wt)):
                for curr_capacity in range(capacity + 1):

                    include = 0
                    if wt[i] <= curr_capacity:
                        include = val[i] + table[curr_capacity - wt[i]]

                    table[curr_capacity] = max(include, table[curr_capacity])
            return table[capacity]

        return unbounded_knapsack(val, wt, capacity)


s = Solution()
print(s.knapSack([1, 2, 3, 5], [1, 4, 7, 10], 8))  # 3
print(s.knapSack([1, 1], [2, 1], 3))  # 3
print(s.knapSack([6, 1, 7, 7], [1, 3, 4, 5], 8))  # 48
print(s.knapSack([6, 8, 7, 100], [2, 3, 4, 5], 1))  # 0
