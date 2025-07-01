# https://www.udemy.com/course/dynamic-programming-algorithms-coding-interview-questions/learn/lecture/38723260#overview


class Solution:
    # def num_fac(self, nums, target):
    #     """
    #     recusive brute force
    #     Time: O(3^n)
    #         m = length of nums
    #         n = target
    #     Space: O(n)
    #     """

    #     def answer(target):
    #         if target < 0:
    #             return 0
    #         if target == 0:
    #             return 1
    #         # # ways 1
    #         result = 0
    #         for num in nums:
    #             result += answer(target - num)
    #         return result

    #         # # ways 2, hard coded
    #         # n0 = answer(target - nums[0])
    #         # n1 = answer(target - nums[1])
    #         # n2 = answer(target - nums[2])
    #         # return n0 + n1 + n2

    #     return answer(target)

    # def num_fac(self, nums, target):
    #     """
    #     Optimized recursive (top-down DP with memoization)
    #     Time: O(m * n)
    #         m = len(nums)
    #         n = target
    #     Space: O(n)
    #     """

    #     def answer(target, memo):
    #         if target < 0:
    #             return 0
    #         if target == 0:
    #             return 1
    #         if memo[target] != -1:
    #             return memo[target]
    #         # # ways 1
    #         result = 0
    #         for num in nums:
    #             result += answer(target - num, memo)
    #         memo[target] = result
    #         return memo[target]

    #         # # ways 2, hard coded
    #         # n0 = answer(target - nums[0])
    #         # n1 = answer(target - nums[1])
    #         # n2 = answer(target - nums[2])
    #         # return n0 + n1 + n2

    #     memo = [-1] * (target + 1)
    #     return answer(target, memo)

    def num_fac(self, nums, target):
        """
        tabular approach
        Time: O(m * n)
            m = len(nums)
            n = target
        Space: O(n)
        """

        table = [-1] * (target + 1)
        table[0] = 1
        for curr_target in range(1, target + 1):
            result = 0
            for num in nums:
                result += table[curr_target - num] if (curr_target - num) >= 0 else 0
            table[curr_target] = result

        return table[target]


s = Solution()
print(s.num_fac([1, 3, 4], 3))  # 2
print(s.num_fac([1, 3, 4], 4))  # 4
print(s.num_fac([1, 3, 4], 5))  # 6
