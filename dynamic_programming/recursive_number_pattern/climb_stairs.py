# https://leetcode.com/problems/climbing-stairs/submissions/1652715523/


class Solution:
    # def climbStairs(self, n: int) -> int:
    #     """
    #     recusive brute force
    #     Time: O(2^n)
    #         n = target value
    #     Space: O(n)
    #     """

    #     def answer(n):

    #         if n < 0:
    #             return 0
    #         if n == 0:
    #             return 1
    #         one_step = answer(n - 1)
    #         two_step = answer(n - 2)
    #         return one_step + two_step

    #     return answer(n)

    # def climbStairs(self, n: int) -> int:
    #     """
    #     optimized recursive with memoization
    #     Time: O(n)
    #         n = target value
    #     Space: O(n)
    #     """

    #     def answer(n, memo):

    #         if n < 0:
    #             return 0
    #         if n == 0:
    #             return 1
    #         if memo[n] != -1:
    #             return memo[n]
    #         one_step = answer(n - 1, memo)
    #         two_step = answer(n - 2, memo)
    #         memo[n] = one_step + two_step
    #         return memo[n]

    #     memo = [-1] * (n + 1)
    #     return answer(n, memo)

    # def climbStairs(self, n: int) -> int:
    #     """
    #     tabular
    #     Time: O(n)
    #         n = target value
    #     Space: O(n)
    #     """

    #     table = [0] * (n + 1)
    #     table[0] = 1
    #     table[1] = 1
    #     for i in range(2, n + 1):
    #         table[i] = table[i - 1] + table[i - 2]

    #     return table[n]

    def climbStairs(self, n: int) -> int:
        """
        tabular constant space
        Time: O(n)
            n = target value
        Space: O(1)
        """
        if n <= 1:
            return n
        one_step = 1
        two_step = 1
        for i in range(2, n + 1):
            combined_step = one_step + two_step
            one_step = two_step
            two_step = combined_step

        return two_step


s = Solution()
print(s.climbStairs(2))  # 2
print(s.climbStairs(3))  # 3
