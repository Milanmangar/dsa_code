# https://leetcode.com/problems/coin-change/


class Solution:
    # def min_coin_change(self, coins, amount):
    #     """
    #     recusive brute force
    #     Time: O(2^n)
    #         n = target amount
    #     Space: O(n)
    #     """

    #     def answer(coins, amount, index):
    #         if index < 0 or amount < 0:
    #             return float("inf")
    #         if amount == 0:
    #             return 0
    #         take = float("inf")
    #         if coins[index] <= amount:
    #             take = answer(coins, amount - coins[index], index)
    #             if take != float("inf"):
    #                 take = 1 + take
    #         not_take = answer(coins, amount, index - 1)
    #         return min(take, not_take)

    #     result = answer(coins, amount, len(coins) - 1)
    #     return result if result != float("inf") else -1

    # def min_coin_change(self, coins, amount):
    #     """
    #     optimized recusive with memoization
    #     Time: O(n * m)
    #         n = target amount
    #         m = len of coins
    #     Space: O(n)
    #     """

    #     def answer(coins, amount, index, memo):
    #         if index < 0 or amount < 0:
    #             return float("inf")
    #         if amount == 0:
    #             return 0
    #         if memo[index][amount] != -1:
    #             return memo[index][amount]
    #         take = float("inf")
    #         if coins[index] <= amount:
    #             take = 1 + answer(coins, amount - coins[index], index, memo)
    #         not_take = answer(coins, amount, index - 1, memo)
    #         memo[index][amount] = min(take, not_take)
    #         return memo[index][amount]

    #     memo = [[-1] * (amount + 1) for _ in range(len(coins))]
    #     result = answer(coins, amount, len(coins) - 1, memo)
    #     return result if result != float("inf") else -1

    # def min_coin_change(self, coins, amount):
    #     """
    #     optimized recusive with memoization
    #     Time: O(n * m)
    #         n = target amount
    #         m = len of coins
    #     Space: O(n)
    #     """

    #     def answer(coins, amount, index, memo):
    #         if index < 0 or amount < 0:
    #             return float("inf")
    #         if amount == 0:
    #             return 0
    #         if memo[index][amount] != -1:
    #             return memo[index][amount]
    #         take = float("inf")
    #         if coins[index] <= amount:
    #             take = 1 + answer(coins, amount - coins[index], index, memo)
    #         not_take = answer(coins, amount, index - 1, memo)
    #         memo[index][amount] = min(take, not_take)
    #         return memo[index][amount]

    #     memo = [[-1] * (amount + 1) for _ in range(len(coins))]
    #     result = answer(coins, amount, len(coins) - 1, memo)
    #     return result if result != float("inf") else -1

    # def min_coin_change(self, coins, amount):
    #     """
    #     optimized with tabulation 2D
    #     Time: O(n * m)
    #         n = target amount
    #         m = len of coins

    #     Space: O(n * m)
    #     """
    #     table = [[float("inf")] * (amount + 1) for _ in range(len(coins))]
    #     for amt in range(0, amount + 1):
    #         if amt % coins[0] == 0:
    #             table[0][amt] = amt // coins[0]
    #     for i in range(1, len(coins)):
    #         for curr_amount in range(amount + 1):
    #             take = float("inf")
    #             if coins[i] <= curr_amount:
    #                 take = 1 + table[i][curr_amount - coins[i]]
    #             not_take = table[i - 1][curr_amount]
    #             table[i][curr_amount] = min(take, not_take)
    #     result = table[len(coins) - 1][amount]
    #     return result if result != float("inf") else -1

    # def min_coin_change(self, coins, amount):
    #     """
    #     optimized with tabulation 1D with temp table
    #     Time: O(n * m)
    #         n = target amount
    #         m = len of coins

    #     Space: O(n)
    #     """
    #     table = [float("inf")] * (amount + 1)
    #     for amt in range(0, amount + 1):
    #         if amt % coins[0] == 0:
    #             table[amt] = amt // coins[0]
    #     for i in range(1, len(coins)):
    #         temp_table = [float("inf")] * (amount + 1)
    #         for curr_amount in range(amount + 1):
    #             take = float("inf")
    #             if coins[i] <= curr_amount:
    #                 take = 1 + temp_table[curr_amount - coins[i]]
    #             not_take = table[curr_amount]
    #             temp_table[curr_amount] = min(take, not_take)
    #         table = temp_table
    #     result = table[amount]
    #     return result if result != float("inf") else -1

    def min_coin_change(self, coins, amount):
        """
        Optimized tabulation with 1D DP array more optimzed
        Time: O(n * m)
            n = amount
            m = len(coins)
        Space: O(n)
        """
        table = [float("inf")] * (amount + 1)
        table[0] = 0  # base case: 0 amount needs 0 coins

        for coin in coins:
            for amt in range(coin, amount + 1):
                if table[amt - coin] != float("inf"):
                    table[amt] = min(table[amt], 1 + table[amt - coin])
                else:
                    print("yes")

        return table[amount] if table[amount] != float("inf") else -1


s = Solution()
# print(s.min_coin_change([1, 2, 5], 11))  # 3
# print(s.min_coin_change([2], 3))  # -1
# print(s.min_coin_change([1], 0))  # 0
print(s.min_coin_change([3, 7, 405, 436], 8839))  # 25
