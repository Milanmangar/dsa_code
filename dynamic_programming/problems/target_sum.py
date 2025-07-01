class Solution:
    # def findTargetSumWays(self, nums: list[int], target: int) -> int:
    # """ bruteforce recursive
    # time: O(2^n), At each of the n indices (where n = len(nums)), you make 2 choices.
    # space: O(n), Maximum recursion depth is n (once per number)
    # """
    # def target_sum_count(index: int, curr_sum: int, nums: list[int], target: int):
    #     if index == len(nums):
    #         if curr_sum == target:
    #             return 1
    #         return 0
    #     positive = target_sum_count(
    #         index + 1, (curr_sum + nums[index]), nums, target
    #     )
    #     negative = target_sum_count(
    #         index + 1, (curr_sum - nums[index]), nums, target
    #     )
    #     return positive + negative

    # return target_sum_count(0, 0, nums, target)

    # def findTargetSumWays(self, nums: list[int], target: int) -> int:
    #     """dictionary memoization
    #     time: O(n * total), n = len(nums), total = sum(nums).
    #     space: O(n × total),  (memo + stack)
    #     """

    #     def target_sum_count(
    #         index: int, curr_sum: int, nums: list[int], target: int, memo: dict
    #     ):
    #         if (index, curr_sum) in memo:
    #             return memo[(index, curr_sum)]
    #         if index == len(nums):
    #             if curr_sum == target:
    #                 return 1
    #             return 0
    #         positive = target_sum_count(
    #             index + 1, (curr_sum + nums[index]), nums, target, memo
    #         )
    #         negative = target_sum_count(
    #             index + 1,
    #             (curr_sum - nums[index]),
    #             nums,
    #             target,
    #             memo,
    #         )
    #         memo[(index, curr_sum)] = positive + negative
    #         return memo[(index, curr_sum)]

    #     return target_sum_count(0, 0, nums, target, {})

    # def findTargetSumWays(self, nums: list[int], target: int) -> int:
    #     """
    #     List-based memoization
    #     Time: O(n * total), where total = sum(nums)
    #     Space: O(n * total)
    #     """

    #     total = sum(nums)
    #     n = len(nums)

    #     # Early return if target is outside the achievable sum range
    #     if abs(target) > total:
    #         return 0

    #     # Create a 2D memoization table with dimensions [n+1][2*total+1]
    #     memo = [[-1 for _ in range(2 * total + 1)] for _ in range(n + 1)]

    #     def target_sum_count(index: int, curr_sum: int) -> int:
    #         offset = total  # to handle negative curr_sum
    #         if memo[index][curr_sum + offset] != -1:
    #             return memo[index][curr_sum + offset]
    #         if index == n:
    #             return 1 if curr_sum == target else 0
    #         positive = target_sum_count(index + 1, curr_sum + nums[index])
    #         negative = target_sum_count(index + 1, curr_sum - nums[index])
    #         memo[index][curr_sum + offset] = positive + negative
    #         return memo[index][curr_sum + offset]

    #     return target_sum_count(0, 0)

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Tabular with Dict
        Time: O(n * total), where total = sum(nums)
        Space: O(n)
        """

        result = {0: 1}
        for num in nums:
            curr_num_sum = {}
            for prev_sum, count in result.items():
                curr_sum_positive = prev_sum + num
                curr_sum_negative = prev_sum - num
                curr_num_sum[curr_sum_positive] = (
                    curr_num_sum.get(curr_sum_positive, 0) + count
                )
                curr_num_sum[curr_sum_negative] = (
                    curr_num_sum.get(curr_sum_negative, 0) + count
                )
            result = curr_num_sum

        return result.get(target, 0)


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
print(s.findTargetSumWays([1, 2, 1], 2))  # 2
print(s.findTargetSumWays([1, 2, 3], 0))  # 2
