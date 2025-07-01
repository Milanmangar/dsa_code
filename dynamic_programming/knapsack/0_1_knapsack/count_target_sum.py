class Solution:

    # def perfectSum(self, nums, k):
    #     """
    #     with brute force recursion
    #     Time Complexity: O(2^n)
    #         For each element, you have two choices: include or exclude
    #         So, total number of recursive calls = 2^n
    #         the check for k == 0 happens only at the base case, but we still explore all branches
    #     Space Complexity: O(n)
    #         The maximum depth of the recursive call stack is n (when all elements are included)
    #     """

    #     def subset_sum(nums: list[int], k: int, index: int) -> int:
    #         if index == len(nums):
    #             return 1 if k == 0 else 0
    #         take = 0
    #         if nums[index] <= k:
    #             take = subset_sum(nums, k - nums[index], index + 1)
    #         not_take = subset_sum(nums, k, index + 1)
    #         return take + not_take

    #     return subset_sum(nums, k, 0)

    # def perfectSum(self, nums, k):
    #     """
    #     with recursion and dict memoization
    #     Time Complexity: O(n * k)
    #         n = len(nums) (number of elements in the list)
    #         k is the target sum.
    #     Space Complexity: O(n * k)
    #         Memoization table stores at most n * k entries.
    #         Call stack can go as deep as O(n) in the worst case (due to recursion).
    #     """

    #     def subset_sum(nums: list[int], k: int, index: int, memo) -> int:
    #         if (index, k) in memo:
    #             return memo[(index, k)]
    #         if index == len(nums):
    #             return 1 if k == 0 else 0
    #         take = 0
    #         if nums[index] <= k:
    #             take = subset_sum(nums, k - nums[index], index + 1, memo)
    #         not_take = subset_sum(nums, k, index + 1, memo)
    #         memo[(index, k)] = take + not_take
    #         return memo[(index, k)]

    #     memo = {}
    #     return subset_sum(nums, k, 0, memo)

    # def perfectSum(self, nums, k):
    #     """
    #     with recursion and list memoization
    #     Time Complexity: O(n * k)
    #         n = len(nums) (number of elements in the list)
    #         k is the target sum.
    #     Space Complexity: O(n * k)
    #         Memoization table stores at most n * k entries.
    #         Call stack can go as deep as O(n) in the worst case (due to recursion).
    #     """

    #     def subset_sum(nums: list[int], k: int, index: int, memo) -> int:
    #         if memo[index][k] != -1:
    #             return memo[index][k]
    #         if index == len(nums):
    #             return 1 if k == 0 else 0
    #         take = 0
    #         if nums[index] <= k:
    #             take = subset_sum(nums, k - nums[index], index + 1, memo)
    #         not_take = subset_sum(nums, k, index + 1, memo)
    #         memo[index][k] = take + not_take
    #         return memo[index][k]

    #     memo = [[-1] * (k + 1) for _ in range(len(nums) + 1)]
    #     return subset_sum(nums, k, 0, memo)

    # def perfectSum(self, nums, k):
    #     """
    #     with tabular and 2D array
    #     Time Complexity: O(n * k)
    #         n = len(nums) (number of elements in the list)
    #         k is the target sum.
    #     Space Complexity: O(n * k)
    #         Memoization table stores at most n * k entries.
    #         Call stack can go as deep as O(n) in the worst case (due to recursion).
    #     """

    #     def subset_sum(nums: list[int], k: int) -> int:
    #         table = [[0] * (k + 1) for _ in range(len(nums) + 1)]
    #         if nums[0] == 0:
    #             table[0][0] = 2  # [], [0]
    #         else:
    #             table[0][0] = 1  # []
    #             if nums[0] <= k:
    #                 table[0][nums[0]] = 1
    #         for i in range(1, len(nums)):
    #             for j in range(k + 1):
    #                 take = 0
    #                 if nums[i] <= j:
    #                     take = table[i - 1][j - nums[i]]
    #                 not_take = table[i - 1][j]
    #                 table[i][j] = take + not_take
    #         return table[len(nums) - 1][k]

    #     return subset_sum(
    #         nums,
    #         k,
    #     )

    def perfectSum(self, nums, k):
        """
        with tabular and 1D array
        Time Complexity: O(n * k)
            n = len(nums) (number of elements in the list)
            k is the target sum.
        Space Complexity: O(n)
            Memoization table stores at most n * k entries.
            Call stack can go as deep as O(n) in the worst case (due to recursion).
        """

        def subset_sum(nums: list[int], k: int) -> int:
            table = [0 for _ in range((k + 1))]
            table[0] = 1
            for i in range(len(nums)):
                for curr_sum in range(k, -1, -1):
                    if curr_sum >= nums[i]:
                        table[curr_sum] = table[curr_sum] + table[curr_sum - nums[i]]
            return table[k]

        return subset_sum(
            nums,
            k,
        )


s = Solution()
print(s.perfectSum([5, 2, 3, 10, 6, 8], 10))  # 3
print(s.perfectSum([2, 5, 1, 4, 3], 10))  # 3
print(s.perfectSum([5, 7, 8], 3))  # 0
print(s.perfectSum([35, 2, 8, 22], 0))  # 0
