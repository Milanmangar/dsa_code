# https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    # def longestCommonSubsequence(self, s1, s2):
    #     """
    #     recursive brute force
    #     Time: O(3 ^ n * m)
    #         Let n be the length of nums.
    #     Space: O(n)
    #     """

    #     # def answer(index_s1, index_s2, count):
    #     #     if index_s1 >= len(s1) or index_s2 >= len(s2):
    #     #         return count
    #     #     c1 = 0
    #     #     if s1[index_s1] == s2[index_s2]:
    #     #         c1 = answer(index_s1 + 1, index_s2 + 1, count + 1)
    #     #     c2 = answer(index_s1, index_s2 + 1, count)
    #     #     c3 = answer(index_s1 + 1, index_s2, count)
    #     #     return max(c1, c2, c3)

    #     def answer(index_s1, index_s2):
    #         if index_s1 >= len(s1) or index_s2 >= len(s2):
    #             return 0
    #         c1 = 0
    #         if s1[index_s1] == s2[index_s2]:
    #             c1 = 1 + answer(index_s1 + 1, index_s2 + 1)
    #             return c1
    #         c2 = answer(index_s1, index_s2 + 1)
    #         c3 = answer(index_s1 + 1, index_s2)
    #         return max(c2, c3)

    #     return answer(0, 0)

    # def longestCommonSubsequence(self, s1, s2):
    #     """
    #     recursive brute force
    #     Time: O(n * m)
    #         Let n be the length of nums.
    #     Space: O(n * m)
    #     """

    #     #     def answer(index_s1, index_s2, count, memo):
    #     #         if index_s1 >= len(s1) or index_s2 >= len(s2):
    #     #             return count
    #     #         if memo[index_s1][index_s2][count] != -1:
    #     #             return memo[index_s1][index_s2][count]
    #     #         c1 = 0
    #     #         if s1[index_s1] == s2[index_s2]:
    #     #             c1 = answer(index_s1 + 1, index_s2 + 1, count + 1, memo)
    #     #         c2 = answer(index_s1, index_s2 + 1, count, memo)
    #     #         c3 = answer(index_s1 + 1, index_s2, count, memo)
    #     #         memo[index_s1][index_s2][count] = max(c1, c2, c3)
    #     #         return memo[index_s1][index_s2][count]

    #     #     n, m = len(s1), len(s2)
    #     #     memo = [[[-1] * min(n, m) for _ in range(m)] for _ in range(n)]
    #     #     return answer(0, 0, 0, memo)

    #     def answer(index_s1, index_s2, memo):
    #         if index_s1 >= len(s1) or index_s2 >= len(s2):
    #             return 0
    #         if memo[index_s1][index_s2] != -1:
    #             return memo[index_s1][index_s2]
    #         c1 = 0
    #         if s1[index_s1] == s2[index_s2]:
    #             c1 = 1 + answer(index_s1 + 1, index_s2 + 1, memo)
    #             memo[index_s1][index_s2] = c1
    #             return c1
    #         c2 = answer(index_s1, index_s2 + 1, memo)
    #         c3 = answer(index_s1 + 1, index_s2, memo)
    #         memo[index_s1][index_s2] = max(c2, c3)
    #         return memo[index_s1][index_s2]

    #     n, m = len(s1), len(s2)
    #     memo = [[-1] * (m + 1) for _ in range(n + 1)]
    #     return answer(0, 0, memo)

    # def longestCommonSubsequence(self, s1, s2):
    #     """
    #     tabular approach 2D
    #     Time: O(n * m)
    #     Space: O(n * m)
    #     """
    #     table = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    #     for i in range(1, len(s1) + 1):
    #         for j in range(1, len(s2) + 1):
    #             if s1[i - 1] == s2[j - 1]:
    #                 table[i][j] = 1 + table[i - 1][j - 1]
    #             else:
    #                 table[i][j] = max(table[i][j - 1], table[i - 1][j])
    #     return table[len(s1)][len(s2)]

    def longestCommonSubsequence(self, s1, s2):
        """
        tabular approach 1D
        Time: O(n * m)
        Space: O(m)
        """
        n, m = len(s1), len(s2)
        prev = [0] * (m + 1)

        for i in range(1, n + 1):
            curr = [0] * (m + 1)
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[m]


s = Solution()
print(s.longestCommonSubsequence("abcde", "ace"))  # 3
print(s.longestCommonSubsequence("abc", "abc"))  # 3
print(s.longestCommonSubsequence("abc", "def"))  # 0
print(s.longestCommonSubsequence("abcde", "ace"))  # 0
# print(s.lcs("YZ", "yz"))  # 0
