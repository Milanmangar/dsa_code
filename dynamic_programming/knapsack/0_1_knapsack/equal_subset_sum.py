# https://leetcode.com/problems/partition-equal-subset-sum/description/


class Solution:

    # def canPartition(self, arr: list[int]) -> bool:
    #     """
    #     brute force recusive
    #     Time Complexity: O(2^n), where n is the length of the array.
    #     Space Complexity: O(n), recursion depth due to the call stack.
    #     """

    #     total = sum(arr)
    #     if total % 2 != 0:
    #         return False
    #     half_sum = total // 2

    #     def answer(arr, index, curr_sum):
    #         if curr_sum == 0:
    #             return True
    #         if index >= len(arr) or curr_sum < 0:
    #             return False
    #         take = answer(arr, index + 1, curr_sum - arr[index])
    #         not_take = answer(arr, index + 1, curr_sum)
    #         if take or not_take:
    #             return True
    #         return False

    #     return answer(arr, 0, half_sum)

    # def canPartition(self, arr: list[int]) -> bool:
    #     """
    #     recursion with dict memoization
    #     Time Complexity: O(n * sum), where n is the length of the array and sum is half of the total sum.
    #     Space Complexity: O(n * sum), for memoization dictionary and recursion stack.
    #     """
    #     total = sum(arr)
    #     if total % 2 != 0:
    #         return False
    #     half_sum = total // 2
    #     memo = {}

    #     def answer(arr, index, curr_sum, memo):
    #         if curr_sum == 0:
    #             return True
    #         if index >= len(arr) or curr_sum < 0:
    #             return False
    #         if (index, curr_sum) in memo:
    #             return memo[(index, curr_sum)]
    #         take = answer(arr, index + 1, curr_sum - arr[index], memo)
    #         not_take = answer(arr, index + 1, curr_sum, memo)
    #         if take or not_take:
    #             memo[(index, curr_sum)] = True
    #             return True
    #         memo[(index, curr_sum)] = False
    #         return False

    #     return answer(arr, 0, half_sum, memo)

    # def canPartition(self, arr: list[int]) -> bool:
    #     """
    #     recursion with list memoization
    #     Time Complexity: O(n * sum), where n is the length of the array and sum is half of the total sum.
    #     Space Complexity: O(n * sum), for the DP table.
    #     """

    #     # code here
    #     total = sum(arr)
    #     if total % 2 != 0:
    #         return False
    #     half_sum = total // 2
    #     table = [[-1] * (half_sum + 1) for _ in range(len(arr) + 1)]

    #     def answer(arr, index, curr_sum, table):
    #         if curr_sum == 0:
    #             return True
    #         if index >= len(arr) or curr_sum < 0:
    #             return False
    #         if table[index][curr_sum] != -1:
    #             return table[index][curr_sum]
    #         take = answer(arr, index + 1, curr_sum - arr[index], table)
    #         not_take = answer(arr, index + 1, curr_sum, table)
    #         if take or not_take:
    #             table[index][curr_sum] = True
    #             return True
    #         table[index][curr_sum] = False
    #         return False

    #     return answer(arr, 0, half_sum, table)

    def canPartition(self, arr: list[int]) -> bool:
        """
        tabular approach 1D
        Time Complexity: O(n * sum), where n is the length of the array and sum is half of the total sum.
        Space Complexity: O(sum), using a 1D DP array.
        """
        total = sum(arr)
        if total % 2 != 0:
            return False
        half_sum = total // 2
        table = [False] * (half_sum + 1)
        table[0] = True
        for i in range(len(arr)):
            for curr_sum in range((len(table) - 1), -1, -1):
                if arr[i] <= curr_sum:
                    table[curr_sum] = table[curr_sum] or table[curr_sum - arr[i]]
        return table[half_sum]


s = Solution()

print(s.canPartition([1, 5, 11, 5]))  # True
print(s.canPartition([1, 2, 3, 5]))  # False
