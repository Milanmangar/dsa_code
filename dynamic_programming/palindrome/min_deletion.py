# https://www.geeksforgeeks.org/problems/minimum-number-of-deletions4610/1


class Solution:

    # def minDeletions(self, s: str) -> int:
    #     """
    #     recursive  brute force, my solution
    #     Time: O(2 ^ n)
    #         n = length of string s
    #     Space: O(n)
    #     """

    #     def answer(start, end):
    #         if start == end or start > end:
    #             return 0
    #         if s[start] == s[end]:
    #             return answer(start + 1, end - 1)
    #         left_skip = 1 + answer(start + 1, end)
    #         right_skip = 1 + answer(start, end - 1)
    #         return min(left_skip, right_skip)

    #     return answer(0, len(s) - 1)

    # def minDeletions(self, s: str) -> int:
    #     """
    #     recursive  brute force, my solution
    #     Time: O(n^2)
    #         n = length of string s
    #     Space: O(n ^ 2)
    #     """

    #     def answer(start, end, memo):
    #         if start == end or start > end:
    #             return 0
    #         if memo[start][end] != -1:
    #             return memo[start][end]
    #         if s[start] == s[end]:
    #             memo[start][end] = answer(start + 1, end - 1, memo)
    #             return memo[start][end]
    #         left_skip = 1 + answer(start + 1, end, memo)
    #         right_skip = 1 + answer(start, end - 1, memo)
    #         memo[start][end] = min(left_skip, right_skip)
    #         return memo[start][end]

    #     memo = [[-1] * len(s) for _ in range(len(s))]
    #     return answer(0, len(s) - 1, memo)

    # def minDeletions(self, s: str) -> int:
    #     """
    #     Tabular approach 2D DP, my solution
    #     Time: O(n^2)
    #     Space: O(n^2)
    #     """
    #     l = len(s)
    #     memo = [[0] * l for _ in range(l)]

    #     for gap in range(1, l):  # gap = j - i
    #         for i in range(l - gap):
    #             j = i + gap
    #             if s[i] == s[j]:
    #                 memo[i][j] = memo[i + 1][j - 1]  # no deletion needed
    #             else:
    #                 pre = 1 + memo[i][j - 1]  # delete s[j]
    #                 suffix = 1 + memo[i + 1][j]  # delete s[i]
    #                 memo[i][j] = min(pre, suffix)

    #     return memo[0][l - 1]

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # def minDeletions(self, s: str) -> int:
    #     """
    #     recursive  brute force, with Longest palindromic subq
    #     Time: O(2 ^ n)
    #         n = length of string s
    #     Space: O(n)
    #     """

    #     def answer(start, end):
    #         if start > end:
    #             return 0
    #         if start == end:
    #             return 1

    #         if s[start] == s[end]:
    #             return 2 + answer(start + 1, end - 1)
    #         left_skip = answer(start + 1, end)
    #         right_skip = answer(start, end - 1)
    #         return max(left_skip, right_skip)

    #     return len(s) - answer(0, len(s) - 1)

    # def minDeletions(self, s: str) -> int:
    #     """
    #     optimized recursive  with memo, with Longest palindromic subq
    #     Time: O(n ^ 2)
    #         n = length of string s
    #     Space: O(n ^ 2)
    #     """
    #     l = len(s)
    #     memo = [[-1] * l for _ in range(l)]

    #     def answer(start, end, memo):
    #         if start > end:
    #             return 0
    #         if start == end:
    #             return 1
    #         if memo[start][end] != -1:
    #             return memo[start][end]

    #         if s[start] == s[end]:
    #             return 2 + answer(start + 1, end - 1, memo)
    #         left_skip = answer(start + 1, end, memo)
    #         right_skip = answer(start, end - 1, memo)
    #         memo[start][end] = max(left_skip, right_skip)
    #         return memo[start][end]

    #     return len(s) - answer(0, len(s) - 1, memo)

    def minDeletions(self, s: str) -> int:
        """
        Tabular approach 2D DP, my solution
        Time: O(n^2)
        Space: O(n^2)
        """
        l = len(s)
        memo = [[0] * l for _ in range(l)]

        for gap in range(l):  # gap = j - i
            for i in range(l - gap):
                j = i + gap
                if gap == 0:
                    memo[i][j] = 1
                elif gap == 1:
                    memo[i][j] = 2 if s[i] == s[j] else 1
                else:
                    if s[i] == s[j]:
                        memo[i][j] = 2 + memo[i + 1][j - 1]  # no deletion needed
                    else:
                        pre = memo[i][j - 1]  # delete s[j]
                        suffix = memo[i + 1][j]  # delete s[i]
                        memo[i][j] = max(pre, suffix)

        return l - memo[0][l - 1]


s = Solution()
print(s.minDeletions("aebcbda"))  # 2
print(s.minDeletions("aba"))  # 0
print(s.minDeletions("kkjmmj"))  # 2
# print(s.minDeletions("abcde" * 20))  # 20
