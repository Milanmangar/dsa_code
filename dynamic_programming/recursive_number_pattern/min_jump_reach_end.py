# https://leetcode.com/problems/jump-game-ii/description/


class Solution:
    # def jump(self, nums):
    #     """
    #     recursive brute force
    #     Time: O(n^n)
    #         Let n be the length of nums.
    #     Space: O(n)
    #     """

    #     def answer(index):
    #         if index >= len(nums) - 1:
    #             return 0
    #         min_jump_result = float("inf")
    #         for i in range((index + 1), min(index + nums[index] + 1, len(nums))):
    #             curr_jump = 1 + answer(i)
    #             min_jump_result = min(min_jump_result, curr_jump)
    #         return min_jump_result

    #     return answer(0)

    # def jump(self, nums):
    #     """
    #     optimized recursive with memoization
    #     Time: O(n^2)
    #         Let n be the length of nums.
    #     Space: O(n)
    #     """

    #     def answer(index, memo):
    #         if index >= len(nums) - 1:
    #             return 0
    #         if memo[index] != -1:
    #             return memo[index]
    #         min_jump_result = float("inf")
    #         for i in range((index + 1), min(index + nums[index] + 1, len(nums))):
    #             curr_jump = 1 + answer(i, memo)
    #             min_jump_result = min(min_jump_result, curr_jump)
    #         memo[index] = min_jump_result
    #         return memo[index]

    #     memo = [-1] * (len(nums) + 1)
    #     return answer(0, memo)

    def jump(self, nums):
        """
        iterative greedy way
        Time: O(n)
            Let n be the length of nums.
        Space: O(1)
        """
        if len(nums) == 1:
            return 0
        total_jumps = 0
        destination = len(nums) - 1
        coverage = 0
        last_jump_index = 0
        for i in range(len(nums)):
            coverage = max(coverage, i + nums[i])
            if i == last_jump_index:
                last_jump_index = coverage
                total_jumps += 1
                if last_jump_index >= destination:
                    return total_jumps

        return total_jumps


s = Solution()
# print(s.jump([7]))  # 0
# print(s.jump([1, 0]))  # 1
# print(s.jump([2, 3, 1, 1, 4]))  # 2
# print(s.jump([2, 1, 1, 1, 4]))  # 3
print(s.jump([2, 4, 1, 2, 3, 1, 1, 2]))  # 3
