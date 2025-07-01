# https://leetcode.com/problems/longest-palindromic-subsequence/submissions/1677038377/
# https://www.youtube.com/watch?v=RiNzHfoA2Lo


class Solution:
    # def longestPalindromeSubseq(self, s: str) -> int:
    #     """
    #     recursive  brute force
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
    #         skip_left = answer(start + 1, end)
    #         skip_right = answer(start, end - 1)
    #         return max(skip_left, skip_right)

    #     return answer(0, len(s) - 1)

    # def longestPalindromeSubseq(self, s: str) -> int:
    #     """
    #     optimized recursive  with memoization
    #     Time: O(n ^ 2)
    #         n = length of string s
    #     Space: O(n ^ 2)
    #     """

    #     def answer(start, end, memo):
    #         if start > end:
    #             return 0
    #         if start == end:
    #             return 1
    #         if memo[start][end] != -1:
    #             return memo[start][end]

    #         if s[start] == s[end]:
    #             memo[start][end] = 2 + answer(start + 1, end - 1, memo)
    #             return memo[start][end]
    #         skip_left = answer(start + 1, end, memo)
    #         skip_right = answer(start, end - 1, memo)
    #         memo[start][end] = max(skip_left, skip_right)
    #         return memo[start][end]

    #     memo = [[-1] * len(s) for _ in range(len(s))]
    #     return answer(0, len(s) - 1, memo)

    def longestPalindromeSubseq(self, s: str) -> int:
        """
        tabular approach 2D
        Time: O(n ^ 2)
            n = length of string s
        Space: O(n ^ 2)
        """

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for g in range(n):  # g is the gap between i and j
            for i in range(n - g):
                j = i + g
                if g == 0:
                    dp[i][j] = 1
                elif g == 1:
                    dp[i][j] = 2 if s[i] == s[j] else 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][n - 1]


s = Solution()
print(s.longestPalindromeSubseq("bbbab"))  # 4
print(s.longestPalindromeSubseq("cbbd"))  # 2
