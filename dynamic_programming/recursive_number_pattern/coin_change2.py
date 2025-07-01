# https://leetcode.com/problems/coin-change-ii/description/


class Solution:
    # def change(self, coins, amount):
    #     """
    #     recusive brute force
    #     Time: O(2^n)
    #         n = target amount
    #     Space: O(n)
    #     """

    #     def answer(coins, amount, index):
    #         if index < 0 or amount < 0:
    #             return 0
    #         if amount == 0:
    #             return 1
    #         take = 0
    #         if coins[index] <= amount:
    #             take = answer(coins, amount - coins[index], index)
    #         not_take = answer(coins, amount, index - 1)
    #         return take + not_take

    #     return answer(coins, amount, len(coins) - 1)

    # def change(self, coins, amount):
    #     """
    #     optimized recusive with memoization
    #     Time: O(n * m)
    #         n = target amount
    #         m = len of coins
    #     Space: O(n)
    #     """

    #     def answer(coins, amount, index, table):
    #         if index < 0 or amount < 0:
    #             return 0
    #         if amount == 0:
    #             return 1
    #         if table[index][amount] != -1:
    #             return table[index][amount]
    #         take = 0
    #         if coins[index] <= amount:
    #             take = answer(coins, amount - coins[index], index, table)
    #         not_take = answer(coins, amount, index - 1, table)
    #         table[index][amount] = take + not_take
    #         return table[index][amount]

    #     table = [[-1] * (amount + 1) for _ in range(len(coins))]
    #     return answer(coins, amount, len(coins) - 1, table)

    # def change(self, coins, amount):
    #     """
    #     optimized tabular 2D starting with 0th index of coins list
    #     Time: O(n * m)
    #         n = target amount
    #         m = len of coins
    #     Space: O(n * m)
    #     """

    #     table = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
    #     for i in range(len(table)):
    #         table[i][0] = 1

    #     for coin_index in range(len(coins)):
    #         for curr_amount in range(amount + 1):
    #             choose = 0
    #             if coins[coin_index] <= curr_amount:
    #                 choose = table[coin_index][curr_amount - coins[coin_index]]
    #             not_choose = table[coin_index - 1][curr_amount]
    #             table[coin_index][curr_amount] = choose + not_choose
    #     return table[len(coins) - 1][curr_amount]

    # def change(self, coins, amount):
    #     """
    #     optimized tabular 2D starting with 1st index of coins list
    #     Time: O(n * m)
    #         n = target amount
    #         m = len of coins
    #     Space: O(n * m)
    #     """
    #     if not coins:
    #         return 0

    #     table = [[0] * (amount + 1) for _ in range(len(coins))]
    #     for i in range(len(coins)):
    #         table[i][0] = 1
    #     for amt in range(1, len(table[0])):
    #         if amt % coins[0] == 0:
    #             table[0][amt] = 1

    #     for coin_index in range(1, len(coins)):
    #         for curr_amount in range(1, amount + 1):
    #             choose = 0
    #             if coins[coin_index] <= curr_amount:
    #                 choose = table[coin_index][curr_amount - coins[coin_index]]
    #             not_choose = table[coin_index - 1][curr_amount]
    #             table[coin_index][curr_amount] = choose + not_choose
    #     return table[len(coins) - 1][amount]

    # def change(self, coins, amount):
    #     """
    #     optimized tabular 1D with temp table
    #     Time: O(n * m)
    #         n = target amount
    #         m = len of coins
    #     Space: O(n * m)
    #     """

    #     table = [0] * (amount + 1)
    #     table[0] = 1
    #     for amt in range(1, len(table)):
    #         if amt % coins[0] == 0:
    #             table[amt] = 1

    #     for coin_index in range(1, len(coins)):
    #         temp_table = [0] * (amount + 1)
    #         temp_table[0] = 1
    #         for curr_amount in range(1, amount + 1):
    #             choose = 0
    #             if coins[coin_index] <= curr_amount:
    #                 choose = temp_table[curr_amount - coins[coin_index]]
    #             not_choose = table[curr_amount]
    #             temp_table[curr_amount] = choose + not_choose
    #         table = temp_table
    #     return table[amount]

    def change(self, coins, amount):
        """
        optimized tabular 1D without temp table
        Time: O(n * m)
            n = target amount
            m = len of coins
        Space: O(n)
        """
        if not coins:
            return 0

        table = [0] * (amount + 1)
        table[0] = 1

        for coin in coins:
            for curr_amount in range(coin, amount + 1):
                table[curr_amount] = table[curr_amount] + table[curr_amount - coin]
        return table[amount]


s = Solution()
print(s.change([1, 2, 5], 5))  # 4
print(s.change([2], 3))  # 0
print(s.change([10], 10))  # 1
print(s.change([3, 5, 7, 8, 9, 10, 11], 500))  # 35502874
