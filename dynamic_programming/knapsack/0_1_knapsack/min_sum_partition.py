import math


class Solution:

    # def minDifference(self, arr):
    #     """
    #     recusive brute force, sum2, sum2
    #     Time: O(2^n)
    #         n: number of elements
    #     Space: O(n)
    #     """
    #     if len(arr) == 1:
    #         return arr[0]

    #     def answer(arr, index, sum1, sum2):

    #         if index == len(arr):
    #             return abs(sum1 - sum2)
    #         left = answer(arr, index + 1, sum1 + arr[index], sum2)
    #         right = answer(arr, index + 1, sum1, sum2 + arr[index])
    #         return min(left, right)

    #     return answer(arr, 0, 0, 0)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # def minDifference(self, arr):
    #     """
    #     recusive brute force, total - curr_sum
    #     Time: O(2^n)
    #         n: number of elements
    #     Space: O(n)
    #     """
    #     if len(arr) == 1:
    #         return arr[0]
    #     total = sum(arr)

    #     def answer(arr, index, curr_sum):

    #         if index == len(arr):
    #             return abs(curr_sum - (total - curr_sum))
    #         left = answer(arr, index + 1, curr_sum + arr[index])
    #         right = answer(arr, index + 1, curr_sum)
    #         return min(left, right)

    #     return answer(arr, 0, 0)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # def minDifference(self, arr):
    #     """
    #     recursive with memoization, sum1, sum2
    #     Time: O(n * total)
    #         n: the length of the array (number of elements).
    #         total: the sum of all elements in the array.
    #     Space: O(n * total)

    #     """
    #     if len(arr) == 1:
    #         return arr[0]
    #     if len(arr) == 2:
    #         return abs(arr[0] - arr[1])
    #     total = sum(arr)
    #     table = [
    #         [[-1 for _ in range(total + 1)] for _ in range(total + 1)]
    #         for _ in range(len(arr) + 1)
    #     ]

    #     def answer(arr, index, sum1, sum2, table):
    #         if table[index][sum1][sum2] != -1:
    #             return table[index][sum1][sum2]

    #         if index == len(arr):
    #             return abs(sum1 - sum2)
    #         left = answer(arr, index + 1, sum1 + arr[index], sum2, table)
    #         right = answer(arr, index + 1, sum1, sum2 + arr[index], table)
    #         table[index][sum1][sum2] = min(left, right)
    #         return table[index][sum1][sum2]

    #     return answer(arr, 0, 0, 0, table)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # def minDifference(self, arr):
    #     """
    #     recursive with memoization, total-curr_sum
    #     Time: O(n * total)
    #         n: the length of the array (number of elements).
    #         total: the sum of all elements in the array.
    #     Space: O(n * total)

    #     best one out of recursion

    #     """
    #     if len(arr) == 1:
    #         return arr[0]
    #     if len(arr) == 2:
    #         return abs(arr[0] - arr[1])
    #     total = sum(arr)
    #     table = [[-1] * (total + 1) for _ in range(len(arr) + 1)]

    #     def answer(arr, index, curr_sum, table):
    #         if table[index][curr_sum] != -1:
    #             return table[index][curr_sum]

    #         if index == len(arr):
    #             return abs(curr_sum - (total - curr_sum))
    #         left = answer(arr, index + 1, curr_sum + arr[index], table)
    #         right = answer(arr, index + 1, curr_sum, table)
    #         table[index][curr_sum] = min(left, right)
    #         return table[index][curr_sum]

    #     return answer(arr, 0, 0, table)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def minDifference(self, arr):
        """
        Tabular approach to minimize the difference between two subset sums.

        Time: O(n * total)
            n: number of elements
            total: sum of all elements
        Space: O(total)
        """
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 2:
            return abs(arr[0] - arr[1])
        total = sum(arr)

        target = total // 2
        table = [False] * (target + 1)
        table[0] = True
        for index in range(0, len(arr)):
            for curr_target in range((len(table) - 1), -1, -1):
                if arr[index] <= curr_target:
                    table[curr_target] = (
                        table[curr_target] or table[curr_target - arr[index]]
                    )
        sub_arr_sum1 = 0
        for curr_target in range((len(table) - 1), -1, -1):
            if table[curr_target]:
                sub_arr_sum1 = curr_target
                break
        sub_arr_sum2 = total - sub_arr_sum1

        return abs(sub_arr_sum1 - sub_arr_sum2)


s = Solution()

print(s.minDifference([1, 6, 11, 5]))  # 1
print(s.minDifference([1, 4]))  # 3
print(s.minDifference([1]))  # 1
