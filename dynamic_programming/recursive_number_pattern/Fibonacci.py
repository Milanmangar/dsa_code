# https://www.udemy.com/course/dynamic-programming-algorithms-coding-interview-questions/learn/lecture/38722946#overview


class Solution:
    # def fib(self, n: int) -> int:
    #     """
    #     recusive brute force
    #     Time: O(2^n)
    #         n = target amount
    #     Space: O(n)
    #     """

    #     def answer(n):
    #         if n == 0 or n == 1:
    #             return n
    #         return answer(n - 1) + answer(n - 2)

    #     return answer(n)

    # def fib(self, n: int) -> int:
    #     """
    #     optimized recusive with memoization

    #     Time: O(n)
    #     Space: O(n)
    #     """

    #     def answer(n, memo):
    #         if n == 0 or n == 1:
    #             return n
    #         if memo[n] != -1:
    #             return memo[n]
    #         memo[n] = answer(n - 1, memo) + answer(n - 2, memo)

    #         return memo[n]

    #     memo = [-1] * (n + 1)
    #     return answer(n, memo)

    # def fib(self, n: int) -> int:
    #     """
    #     tabular 1D

    #     Time: O(n)
    #     Space: O(n)
    #     """
    #     if n <= 1:
    #         return n
    #     answer = [-1] * (n + 1)
    #     answer[0], answer[1] = 0, 1
    #     for i in range(2, n + 1):
    #         answer[i] = answer[i - 1] + answer[i - 2]

    #     return answer[n]

    def fib(self, n: int) -> int:
        """
        constant space

        Time: O(n)
        Space: O(1)
        """
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c

        return b


s = Solution()
print(s.fib(2))  # 1
print(s.fib(3))  # 2
print(s.fib(4))  # 3
