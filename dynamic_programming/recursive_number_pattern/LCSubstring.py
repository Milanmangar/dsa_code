class Solution:
    # def lcs(self, s1, s2):
    #     """
    #     recursive brute force
    #     Time: O(3 ^ n * m)
    #         Let n be the length of nums.
    #     Space: O(n)
    #     """

    #     def longestCommonSubstr(s1_index, s2_index, count):
    #         if s1_index >= len(s1) or s2_index >= len(s2):
    #             return count
    #         same_letter_count = count
    #         if s1[s1_index] == s2[s2_index]:
    #             same_letter_count = longestCommonSubstr(
    #                 s1_index + 1, s2_index + 1, count + 1
    #             )
    #         skip_s2_count = longestCommonSubstr(s1_index, s2_index + 1, 0)
    #         skip_s1_count = longestCommonSubstr(s1_index + 1, s2_index, 0)
    #         return max(same_letter_count, skip_s2_count, skip_s1_count)

    # return longestCommonSubstr(0, 0, 0)

    # def lcs(self, s1, s2):
    #     """
    #     Longest Common Substring (Recursive with Memoization)
    #     Time: O(n * m * min(n, m))
    #     Space: O(n * m * min(n, m))
    #     """

    #     def longestCommonSubstr(s1_index, s2_index, count, memo):

    #         if s1_index >= len(s1) or s2_index >= len(s2):
    #             return count

    #         if memo[s1_index][s2_index][count] != -1:
    #             return memo[s1_index][s2_index][count]
    #         same_letter_count = count
    #         if s1[s1_index] == s2[s2_index]:
    #             same_letter_count = longestCommonSubstr(
    #                 s1_index + 1, s2_index + 1, count + 1, memo
    #             )
    #         skip_s2_count = longestCommonSubstr(s1_index, s2_index + 1, 0, memo)
    #         skip_s1_count = longestCommonSubstr(s1_index + 1, s2_index, 0, memo)
    #         memo[s1_index][s2_index][count] = max(
    #             same_letter_count, skip_s2_count, skip_s1_count
    #         )
    #         return memo[s1_index][s2_index][count]

    #     l = max(len(s1), len(s2))
    #     n, m = len(s1), len(s2)
    #     memo = [[[-1 for _ in range(min(n, m))] for _ in range(m)] for _ in range(n)]
    #     return longestCommonSubstr(0, 0, 0, memo)

    # def lcs(self, s1, s2):
    #     """
    #     tabular approach 2D
    #     Time: O(n * m)
    #     Space: O(n * m)
    #     """
    #     table = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    #     max_val = 0
    #     for i in range(1, len(s1) + 1):
    #         for j in range(1, len(s2) + 1):
    #             if s1[i - 1] == s2[j - 1]:
    #                 table[i][j] = 1 + table[i - 1][j - 1]
    #                 max_val = max(max_val, table[i][j])

    #     return max_val

    def lcs(self, s1, s2):
        """
        tabular approach 1D
        Time: O(n * m)
        Space: O(n * m)
        """
        m, n = len(s1), len(s2)
        prev = [0] * (n + 1)
        max_val = 0
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                    max_val = max(max_val, curr[j])
            prev = curr

        return max_val


s = Solution()
print(s.lcs("adac", "adadac"))  # 4
# print(s.lcs("ABCDGH", "ACDGHR"))  # 4
# print(s.lcs("abc", "acb"))  # 1
# print(s.lcs("YZ", "yz"))  # 0
