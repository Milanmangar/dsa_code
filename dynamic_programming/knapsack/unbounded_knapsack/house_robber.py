# https://leetcode.com/problems/house-robber/description/
# https://www.youtube.com/watch?v=GrMBfJNk_NY


class Solution:
    # def rob(self, nums: list[int]) -> int:
    #     """
    #     recusive brute force
    #     Time: O(2^n)
    #         n = length of nums
    #     Space: O(n)
    #     """

    #     def answer(index):
    #         if index < 0:
    #             return 0
    #         rob = answer(index - 1)
    #         not_rob = nums[index] + answer(index - 2)
    #         return max(rob, not_rob)

    #     return answer(len(nums) - 1)

    # def rob(self, nums: list[int]) -> int:
    #     """
    #     recusive brute force
    #     Time: O(n)
    #         n = length of nums
    #     Space: O(n)
    #     """

    #     def answer(index, memo):
    #         if memo[index] != -1:
    #             return memo[index]
    #         if index == 0:
    #             return nums[index]
    #         if index < 0:
    #             return 0
    #         rob = answer(index - 1, memo)
    #         not_rob = nums[index] + answer(index - 2, memo)
    #         memo[index] = max(rob, not_rob)
    #         return memo[index]

    #     memo = [-1] * len(nums)
    #     return answer(len(nums) - 1, memo)

    # def rob(self, nums: list[int]) -> int:
    #     """
    #     tabular approach
    #     Time: O(n)
    #         n = length of nums
    #     Space: O(n)
    #     """
    #     table = [0] * (len(nums) + 1)
    #     table[0] = nums[0]
    #     for i in range(1, len(nums)):
    #         take = nums[i]
    #         if i > 1:
    #             take += table[i - 2]
    #         not_take = table[i - 1]
    #         table[i] = max(take, not_take)
    #     return table[len(nums) - 1]

    def rob(self, nums: list[int]) -> int:
        """
        tabular approach
        Time: O(n)
            n = length of nums
        Space: O(1)
        """
        if len(nums) == 1:
            return nums[0]

        prev1 = nums[0]
        prev2 = 0
        for i in range(1, len(nums)):
            take = nums[i]
            if i > 1:
                take += prev2
            not_take = prev1

            curr_i = max(take, not_take)
            prev2 = prev1
            prev1 = curr_i
        return prev1


s = Solution()
print(s.rob([1, 2, 3, 1]))  # 4
print(s.rob([2, 7, 9, 3, 1]))  # 12
print(s.rob([2, 1]))  # 2
print(s.rob([2, 1, 1, 2]))  # 4
