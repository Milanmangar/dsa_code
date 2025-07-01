# https://www.udemy.com/course/dynamic-programming-algorithms-coding-interview-questions/learn/lecture/38723264#overview


class Solution:
    # def score(self, target):
    #     """
    #     recusive brute force
    #     Time: O(3^n)
    #         n = target
    #     Space: O(n)
    #     """

    #     def answer(target):
    #         if target < 0:
    #             return 0
    #         if target == 0:
    #             return 1
    #         # hardcoding it because on points 1, 2, 4 can be given per score
    #         p1 = answer(target - 1)
    #         p2 = answer(target - 2)
    #         p4 = answer(target - 4)
    #         return p1 + p2 + p4

    # def score(self, target):
    #     """
    #     optimized recusive brute force
    #     Time: O(n)
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
    #         # hardcoding it because on points 1, 2, 4 can be given per score
    #         p1 = answer(target - 1, memo)
    #         p2 = answer(target - 2, memo)
    #         p4 = answer(target - 4, memo)
    #         memo[target] = p1 + p2 + p4
    #         return memo[target]

    #     memo = [-1] * (target + 1)
    #     return answer(target, memo)

    # def score(self, target):
    #     """
    #     tabular approach
    #     Time: O(n)
    #         n = target
    #     Space: O(n)
    #     """

    #     table = [0] * (target + 1)
    #     table[0] = 1
    #     for curr_target in range(1, target + 1):
    #         p1 = table[curr_target - 1] if (curr_target - 1) >= 0 else 0
    #         p2 = table[curr_target - 2] if (curr_target - 2) >= 0 else 0
    #         p4 = table[curr_target - 4] if (curr_target - 4) >= 0 else 0
    #         table[curr_target] = p1 + p2 + p4
    #     return table[target]

    def score(self, target):
        if target < 0:
            return 0
        if target == 0:
            return 1

        # Initialize score(0) to score(3)
        dp0 = 1  # score(0)
        dp1 = 1  # score(1) = score(0)
        dp2 = dp1 + dp0  # score(2) = score(1) + score(0)
        dp3 = dp2 + dp1  # score(3) = score(2) + score(1)

        if target == 1:
            return dp1
        if target == 2:
            return dp2
        if target == 3:
            return dp3

        for i in range(4, target + 1):
            current = dp3 + dp2 + dp0  # score(i) = score(i-1) + score(i-2) + score(i-4)
            dp0, dp1, dp2, dp3 = dp1, dp2, dp3, current

        return dp3


s = Solution()
print(s.score(0))  # 1
print(s.score(1))  # 1
print(s.score(2))  # 2
print(s.score(3))  # 3
print(s.score(4))  # 6
print(s.score(5))  # 10
print(s.score(6))  # 18
print(s.score(7))  # 31
print(s.score(8))  # 55
print(s.score(9))  # 96
print(s.score(10))  # 169
