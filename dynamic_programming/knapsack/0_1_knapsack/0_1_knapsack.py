# resource: https://www.udemy.com/course/dynamic-programming-algorithms-coding-interview-questions/learn/lecture/34922645#overview
# problem: https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1


class Solution:

    # def knapsack(self, W, val, wt):
    #     """brute for recursive, time: O(2ⁿ), space: O(n) (recursive stack space)
    #     n be the number of items (len(wt))
    #     W be the total capacity of the knapsack
    #     """
    #     return self.answer(wt, val, W, len(wt))

    # def answer(
    #     self,
    #     weights: list,
    #     values: list,
    #     capacity: int,
    #     index: int,
    # ) -> int:
    #     if index == 0 or capacity == 0:
    #         return 0
    #     chose = 0
    #     if weights[index - 1] <= capacity:
    #         chose = values[index - 1] + self.answer(
    #             weights, values, (capacity - weights[index - 1]), (index - 1)
    #         )
    #     not_chose = self.answer(weights, values, capacity, (index - 1))
    #     return max(chose, not_chose)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # def knapsack(self, W, val, wt):
    #     """recursive with memoization but staring from 0th index instead on nth index,
    #     recommended is nth index for dynamic programming
    #     time: O(n × W)
    #         n = len(wt) (number of items)
    #         W is the total capacity of the knapsack
    #         Each subproblem (index, capacity) is computed at most once due to memoization.
    #     space: O(n × W)
    #         The maximum recursion depth is O(n), so: Space=O(n×W)+O(n)=O(n×W)
    #         We usually drop the smaller O(n) when analyzing asymptotic complexity.
    #     """
    #     memo = [[-1] * (W + 1) for _ in range(len(wt) + 1)]
    #     return self.answer(wt, val, W, 0, memo)

    # def answer(
    #     self,
    #     weights: list,
    #     values: list,
    #     capacity: int,
    #     index: int,
    #     memo: list[list[int]],
    # ) -> int:

    #     if memo[index][capacity] != -1:
    #         return memo[index][capacity]
    #     if index > (len(weights) - 1) or capacity == 0:
    #         return 0
    #     chose = 0
    #     if weights[index] <= capacity:
    #         chose = values[index] + self.answer(
    #             weights, values, (capacity - weights[index]), (index + 1), memo
    #         )
    #     not_chose = self.answer(weights, values, capacity, (index + 1), memo)
    #     memo[index][capacity] = max(chose, not_chose)
    #     return memo[index][capacity]

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # def knapsack(self, W, val, wt):
    #     """recursive with memoization,
    #     time: O(n × W)
    #         n = len(wt) (number of items)
    #         W is the total capacity of the knapsack
    #         Each subproblem (index, capacity) is computed at most once due to memoization.
    #     space: O(n × W)
    #         The maximum recursion depth is O(n), so: Space=O(n×W)+O(n)=O(n×W)
    #         We usually drop the smaller O(n) when analyzing asymptotic complexity.
    #     """
    #     memo = [[-1] * (W + 1) for _ in range(len(wt) + 1)]
    #     return self.answer(wt, val, W, len(wt), memo)

    # def answer(
    #     self,
    #     weights: list,
    #     values: list,
    #     capacity: int,
    #     index: int,
    #     memo: list[list[int]],
    # ) -> int:

    #     if memo[index][capacity] != -1:
    #         return memo[index][capacity]
    #     if index == 0 or capacity == 0:
    #         return 0
    #     chose = 0
    #     if weights[index - 1] <= capacity:
    #         chose = values[index - 1] + self.answer(
    #             weights, values, (capacity - weights[index - 1]), (index - 1), memo
    #         )
    #     not_chose = self.answer(weights, values, capacity, (index - 1), memo)
    #     memo[index][capacity] = max(chose, not_chose)
    #     return memo[index][capacity]

    # def knapsack(self, W, val, wt):
    #     """with 2D array tabulation,
    #     time: O(n × W)
    #         n = len(wt) (number of items)
    #         W is the total capacity of the knapsack
    #         Each subproblem (index, capacity) is computed at most once due to memoization.
    #     space: O(n × W)
    #         The maximum recursion depth is O(n), so: Space=O(n×W)+O(n)=O(n×W)
    #         We usually drop the smaller O(n) when analyzing asymptotic complexity.
    #     """
    #     return self.answer(wt, val, W)

    # def answer(
    #     self,
    #     weights: list,
    #     values: list,
    #     capacity: int,
    # ) -> int:

    #     table: list[list[int]] = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]

    #     for i in range(1, len(weights) + 1):
    #         for j in range(capacity + 1):
    #             take = 0
    #             if weights[i - 1] <= j:
    #                 take = values[i - 1] + table[i - 1][j - weights[i - 1]]
    #             not_take = table[i - 1][j]
    #             table[i][j] = max(take, not_take)
    #     return table[len(weights)][capacity]

    def knapsack(self, W, val, wt):
        """with 1D array tabulation,
        time: O(n × W)
            n = len(wt) (number of items)
            W is the total capacity of the knapsack
            Each subproblem (index, capacity) is computed at most once due to memoization.
        space: O(n)
            The maximum recursion depth is O(n), so: Space=O(n)
        """
        return self.answer(wt, val, W)

    def answer(
        self,
        weights: list,
        values: list,
        capacity: int,
    ) -> int:

        table: list[int] = [0 for _ in range(capacity + 1)]

        for i in range(0, len(weights)):
            for j in range((capacity), -1, -1):
                if weights[i] <= j:
                    table[j] = max(table[j], values[i] + (table[j - weights[i]]))
        return table[capacity]


s = Solution()
print(s.knapsack(4, [1, 2, 3], [4, 5, 1]))  # 3
print(s.knapsack(3, [1, 2, 3], [4, 5, 6]))  # 0
print(s.knapsack(5, [10, 40, 30, 50], [5, 4, 2, 3]))  # 80
print(s.knapsack(5, [10, 15, 40], [1, 2, 3]))  # 55
print(
    s.knapsack(6, [5, 10, 7, 5, 1, 1, 5, 4, 5, 8], [4, 4, 1, 1, 2, 6, 4, 4, 4, 6])
)  # 22

print(s.knapsack(9000, [10, 40, 30, 50] * 20, [5, 4, 2, 3] * 20))  # 2600
