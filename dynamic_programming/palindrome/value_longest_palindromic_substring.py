class Solution:
    # def longestPalindrome(self, s):
    #     """
    #     recursive  brute force, my solution
    #     Time: O(2 ^ n)
    #         n = length of string s
    #     Space: O(n)
    #     """
    #     result = ""

    #     def answer(start, end):
    #         nonlocal result
    #         # base case
    #         if start == end:
    #             return 1
    #         if start > end:
    #             return 0

    #         # recursive case
    #         if s[start] == s[end]:
    #             inner = answer(start + 1, end - 1)
    #             if inner == end - start - 1:
    #                 result = (
    #                     s[start : end + 1]
    #                     if len(s[start : end + 1]) > len(result)
    #                     else result
    #                 )
    #                 return end - start + 1

    #         left = answer(start + 1, end)
    #         right = answer(start, end - 1)
    #         return max(left, right)

    #     answer(0, len(s) - 1)

    #     return result if len(result) > 0 else s[0]

    # def longestPalindrome(self, s):
    #     """
    #     optimized recursive with memo, my solution
    #     Time: O(n ^ 2)
    #         n = length of string s
    #     Space: O(n ^ 2)
    #     """
    #     result = ""

    #     def answer(start, end, memo):
    #         nonlocal result
    #         # base case
    #         if start == end:
    #             return 1
    #         if start > end:
    #             return 0
    #         if memo[start][end] != -1:
    #             return memo[start][end]

    #         # recursive case
    #         if s[start] == s[end]:
    #             inner = answer(start + 1, end - 1, memo)
    #             if inner == end - start - 1:
    #                 result = (
    #                     s[start : end + 1]
    #                     if len(s[start : end + 1]) > len(result)
    #                     else result
    #                 )
    #                 memo[start][end] = end - start + 1
    #                 return memo[start][end]

    #         left = answer(start + 1, end, memo)
    #         right = answer(start, end - 1, memo)
    #         memo[start][end] = max(left, right)
    #         return memo[start][end]

    #     l = len(s)
    #     memo = [[-1] * l for _ in range(l)]
    #     answer(0, len(s) - 1, memo)

    #     return result if len(result) > 0 else s[0]

    def longestPalindrome(self, s):
        """
        Tabular 2D DP for Longest Palindromic Substring.
        Time: O(n^2), Space: O(n^2)
        Returns the longest palindromic substring.
        """
        n = len(s)
        if n == 0:
            return ""

        table = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        for gap in range(n):
            for i in range(n - gap):
                j = i + gap
                if gap == 0:
                    table[i][j] = True
                elif gap == 1:
                    table[i][j] = s[i] == s[j]
                else:
                    table[i][j] = (s[i] == s[j]) and table[i + 1][j - 1]

                if table[i][j] and (gap + 1) > max_len:
                    max_len = gap + 1
                    start = i

        return s[start : start + max_len]


s = Solution()
# print(s.longestPalindrome("abcbb"))
# # print(s.longestPalindrome("abcbq"))
# print(s.longestPalindrome("c"))
# print(s.longestPalindrome("xyz"))
print(s.longestPalindrome("afternoon"))
