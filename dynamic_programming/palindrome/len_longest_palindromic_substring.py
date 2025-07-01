class Solution:
    # def LPsubstring(self, s):
    #     """
    #     recursive  brute force
    #     Time: O(2 ^ n)
    #         n = length of string s
    #     Space: O(n)
    #     """

    #     def answer(start, end):
    #         # base case
    #         if start == end:
    #             return 1
    #         if start > end:
    #             return 0

    #         # recursive case
    #         if s[start] == s[end]:
    #             inner = answer(start + 1, end - 1)
    #             if inner == end - start - 1:
    #                 return end - start + 1

    #         left = answer(start + 1, end)
    #         right = answer(start, end - 1)
    #         return max(left, right)

    #     return answer(0, len(s) - 1)

    # def LPsubstring(self, s):
    #     """
    #     optmized recursive with memo
    #     Time: O(n ^ 2)
    #         n = length of string s
    #     Space: O(n ^ 2)
    #     """

    #     def answer(start, end, memo):
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
    #                 memo[start][end] = end - start + 1
    #                 return memo[start][end]

    #         left = answer(start + 1, end, memo)
    #         right = answer(start, end - 1, memo)
    #         memo[start][end] = max(left, right)
    #         return memo[start][end]

    #     l = len(s)
    #     memo = [[-1] * l for _ in range(l)]
    #     return answer(0, l - 1, memo)

    def LPsubstring(self, s):
        """
        Tabular 2D DP for Longest Palindromic Substring
        Time: O(n^2)
        Space: O(n^2)
        Returns the length of the longest palindromic substring.
        """
        l = len(s)
        if l == 0:
            return 0

        table = [[False] * l for _ in range(l)]
        max_len = 1  # At least every single char is a palindrome

        for gap in range(l):
            for i in range(l - gap):
                j = i + gap
                if gap == 0:
                    table[i][j] = True
                elif gap == 1:
                    if s[i] == s[j]:
                        table[i][j] = True
                        max_len = 2
                else:
                    if s[i] == s[j] and table[i + 1][j - 1] is True:
                        table[i][j] = True
                        max_len = max(max_len, gap + 1)

        return max_len


s = Solution()
print(s.LPsubstring("afternoon"))
# print(s.LPsubstring("abcbb"))
# print(s.LPsubstring("abcbq"))
# print(s.LPsubstring("abcbbaobb"))
# print(s.LPsubstring("xyz"))
